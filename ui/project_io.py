from __future__ import annotations

import re
import shutil
import tempfile
from pathlib import Path


class _LocalPathUpload:
    def __init__(self, path: Path):
        self.path = path
        self.name = path.name
        self.size = path.stat().st_size

    def read(self) -> bytes:
        return self.path.read_bytes()


def _existing_hsf_root(proj) -> Path | None:
    raw_root = getattr(proj, "root", None)
    if not raw_root:
        return None
    root = Path(raw_root).expanduser().resolve()
    if not root.is_dir():
        return None
    if (root / "libpartdata.xml").exists() or (root / "scripts").is_dir():
        return root
    return None


def _format_compile_result(*, result, output_gsm: str, compiler_mode: str, hsf_dir: str | Path | None = None) -> tuple[bool, str]:
    mock_tag = " [Mock]" if compiler_mode.startswith("Mock") else ""
    if result.success:
        msg = f"✅ **Compile successful{mock_tag}**\n\n📦 GSM: `{output_gsm}`"
        if hsf_dir:
            msg += f"\n\n📁 HSF source directory: `{hsf_dir}`"
        if compiler_mode.startswith("Mock"):
            msg += "\n\n⚠️ Mock mode does not produce a real .gsm; switch to LP_XMLConverter for real compilation."
        return True, msg

    return False, f"❌ **Compile failed**\n\n```\n{result.stderr[:500]}\n```"


def _max_existing_gsm_revision_in_dir(proj_name: str, output_dir: str | Path) -> int:
    out_dir = Path(output_dir).expanduser()
    if not out_dir.exists():
        return 0

    pattern = re.compile(rf"^{re.escape(proj_name)}_v(\d+)\.gsm$", re.IGNORECASE)
    max_rev = 0
    for path in out_dir.glob(f"{proj_name}_v*.gsm"):
        match = pattern.match(path.name)
        if not match:
            continue
        try:
            max_rev = max(max_rev, int(match.group(1)))
        except ValueError:
            continue
    return max_rev


_INVALID_HSF_NAME_RE = re.compile(r'[\\/:*?"<>|\x00-\x1f]+')


def sanitize_hsf_project_name(raw: str, fallback: str = "") -> str:
    name = _INVALID_HSF_NAME_RE.sub("_", str(raw or "").strip())
    name = re.sub(r"\s+", "_", name)
    name = re.sub(r"_+", "_", name)
    return name.strip(" ._-") or fallback


def _versioned_gsm_path_in_dir(proj_name: str, output_dir: str | Path, revision: int) -> str:
    out_dir = Path(output_dir).expanduser()
    out_dir.mkdir(parents=True, exist_ok=True)
    return str(out_dir / f"{proj_name}_v{revision}.gsm")


def save_project_to_hsf_dir(
    proj,
    parent_dir: str,
    hsf_name: str,
    *,
    source_root: str | Path | None = None,
) -> tuple[bool, str, Path | None]:
    if proj is None:
        return False, "❌ No project available to save", None

    parent = Path(str(parent_dir or "")).expanduser()
    if not str(parent_dir or "").strip():
        return False, "❌ Please select a save directory", None
    if not parent.exists():
        try:
            parent.mkdir(parents=True, exist_ok=True)
        except Exception as exc:
            return False, f"❌ Could not create save directory: {exc}", None
    if not parent.is_dir():
        return False, f"❌ Not a directory: {parent}", None
    parent = parent.resolve()

    project_name = sanitize_hsf_project_name(hsf_name, fallback="")
    if not project_name:
        return False, "❌ Please enter an HSF folder name", None

    target_root = (parent / project_name).expanduser().resolve()
    if target_root.exists() and not target_root.is_dir():
        return False, f"❌ Target path is not a directory: {target_root}", None

    current_root = None
    raw_root = getattr(proj, "root", None)
    if raw_root:
        current_root = Path(raw_root).expanduser().resolve()
    previous_source = Path(source_root).expanduser().resolve() if source_root else None

    allowed_existing_roots = {root for root in (current_root, previous_source) if root is not None}
    if target_root.exists() and target_root not in allowed_existing_roots:
        has_contents = any(target_root.iterdir())
        if has_contents:
            return False, f"❌ Target HSF directory already exists and is not empty: {target_root}", None

    proj.name = project_name
    proj.work_dir = parent
    proj.root = target_root
    saved_root = Path(proj.save_to_disk()).expanduser().resolve()

    if previous_source is not None and previous_source.exists() and previous_source != saved_root:
        try:
            from openbrep.revisions import copy_project_metadata

            copy_project_metadata(previous_source, saved_root)
        except Exception:
            pass

    return True, f"✅ HSF project saved: `{saved_root}`", saved_root


def _prepare_project_for_compile(proj, gsm_name: str, work_dir: str) -> None:
    project_name = str(getattr(proj, "name", "") or "").strip()
    output_name = str(gsm_name or "").strip()
    existing_root = _existing_hsf_root(proj)

    if (not project_name or project_name == "untitled") and output_name:
        proj.name = output_name
        project_name = output_name

    if existing_root is not None:
        if hasattr(proj, "work_dir"):
            proj.work_dir = existing_root.parent
        if hasattr(proj, "root"):
            proj.root = existing_root
        return

    compile_work_dir = Path(work_dir)
    if hasattr(proj, "work_dir"):
        proj.work_dir = compile_work_dir
    if hasattr(proj, "root") and project_name:
        proj.root = compile_work_dir / project_name


def do_compile(
    proj,
    gsm_name: str,
    instruction: str = "",
    *,
    session_state,
    safe_compile_revision_fn,
    versioned_gsm_path_fn,
    get_compiler_fn,
    compiler_mode: str,
    output_dir: str | None = None,
    format_compile_result_fn=None,
) -> tuple:
    format_compile_result_fn = format_compile_result_fn or _format_compile_result
    try:
        work_dir = str(session_state.work_dir)
        _prepare_project_for_compile(proj, gsm_name, work_dir)
        compile_name = gsm_name or proj.name

        requested_rev = int(session_state.get("script_revision", 0)) or 1
        if output_dir:
            compile_rev = max(
                requested_rev,
                _max_existing_gsm_revision_in_dir(compile_name, output_dir) + 1,
            )
        else:
            compile_rev = safe_compile_revision_fn(compile_name, work_dir, requested_rev)
        if compile_rev != requested_rev:
            session_state.script_revision = compile_rev
        if output_dir:
            output_gsm = _versioned_gsm_path_in_dir(compile_name, output_dir, compile_rev)
        else:
            output_gsm = versioned_gsm_path_fn(compile_name, work_dir, revision=compile_rev)
        hsf_dir = proj.save_to_disk()
        result = get_compiler_fn().hsf2libpart(str(hsf_dir), output_gsm)

        ok, msg = format_compile_result_fn(
            result=result,
            output_gsm=output_gsm,
            compiler_mode=compiler_mode,
            hsf_dir=hsf_dir,
        )
        session_state.compile_log.append({
            "project": proj.name,
            "instruction": instruction,
            "success": bool(result.success),
            "attempts": 1,
            "message": "Success" if result.success else result.stderr,
        })
        return ok, msg
    except Exception as e:
        return False, f"❌ **Error**: {str(e)}"


def import_gsm(
    gsm_bytes: bytes,
    filename: str,
    *,
    get_compiler_fn,
    mock_compiler_class,
    work_dir: str,
) -> tuple:
    compiler = get_compiler_fn()

    if isinstance(compiler, mock_compiler_class):
        return None, "❌ GSM import requires LP_XMLConverter; Mock mode is not supported. Please select LP mode in the sidebar and specify the path."

    bin_path = compiler.converter_path or "(not detected)"
    if not compiler.is_available:
        return (
            None,
            f"❌ LP_XMLConverter not found\n\n"
            f"Detected path: `{bin_path}`\n\n"
            f"Example of a correct macOS path:\n"
            f"`/Applications/GRAPHISOFT/ArchiCAD 28/LP_XMLConverter.app/Contents/MacOS/LP_XMLConverter`\n\n"
            f"Please enter the correct path manually in the sidebar.",
        )

    tmp = Path(tempfile.mkdtemp())
    gsm_path = tmp / filename
    gsm_path.write_bytes(gsm_bytes)
    hsf_out = tmp / "hsf_out"
    hsf_out.mkdir()

    result = compiler.libpart2hsf(str(gsm_path), str(hsf_out))

    if not result.success:
        diag = result.stderr or result.stdout or "(no output)"
        shutil.rmtree(tmp, ignore_errors=True)
        # Append Windows-specific diagnostics
        extra = ""
        import platform
        if platform.system() == "Windows":
            extra = (
                f"\n\n**Windows diagnostics**:\n"
                f"- Path exists: {Path(compiler.converter_path).exists() if compiler.converter_path else False}\n"
                f"- Is a file: {Path(compiler.converter_path).is_file() if compiler.converter_path else False}\n"
                f"- Extension: {Path(compiler.converter_path).suffix if compiler.converter_path else ''}\n"
            )
        return (
            None,
            f"❌ GSM unpacking failed (exit={result.exit_code})\n\n"
            f"**Binary**: `{bin_path}`\n\n"
            f"**Output**:\n```\n{diag[:800]}\n```{extra}",
        )

    try:
        def _find_hsf_root(base: Path) -> Path:
            if (base / "libpartdata.xml").exists():
                return base
            if (base / "scripts").is_dir():
                return base
            for d in sorted(base.iterdir()):
                if d.is_dir() and (d / "libpartdata.xml").exists():
                    return d
            for d in sorted(base.iterdir()):
                if d.is_dir() and (d / "scripts").is_dir():
                    return d
            subdirs = [d for d in base.iterdir() if d.is_dir()]
            return subdirs[0] if subdirs else base

        hsf_dir = _find_hsf_root(hsf_out)

        if not hsf_dir.exists():
            contents = list(hsf_out.iterdir())
            shutil.rmtree(tmp, ignore_errors=True)
            return (
                None,
                f"❌ Could not locate HSF root directory\n\n"
                f"hsf_out contents: `{[str(c.name) for c in contents]}`\n\n"
                f"stdout: {result.stdout[:300]}\nstderr: {result.stderr[:300]}",
            )

        gsm_stem = Path(filename).stem
        project_dir = Path(work_dir) / gsm_stem
        suffix = 1
        while project_dir.exists():
            suffix += 1
            project_dir = Path(work_dir) / f"{gsm_stem}_imported_{suffix}"
        shutil.copytree(hsf_dir, project_dir)

        from openbrep.hsf_project import HSFProject

        hsf_files = sorted(str(p.relative_to(project_dir)) for p in project_dir.rglob("*") if p.is_file())
        loaded_proj = HSFProject.load_from_disk(str(project_dir))
        scripts_found = [s.value for s in loaded_proj.scripts]
        diag = (
            f"\n\n**HSF file list**: `{hsf_files}`"
            f"\n**Recognized scripts**: `{scripts_found}`"
        )
        return (
            project_dir,
            f"✅ Imported `{loaded_proj.name}` — {len(loaded_proj.parameters)} parameters, {len(loaded_proj.scripts)} scripts{diag}",
        )
    except Exception as e:
        return None, f"❌ HSF parse failed: {e}"
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def handle_hsf_directory_load(
    project_dir: str,
    *,
    normalize_pasted_path_fn,
    load_project_from_disk_fn,
    finalize_loaded_project_fn,
) -> tuple[bool, str]:
    raw_path = normalize_pasted_path_fn(project_dir)
    if not raw_path:
        return False, "❌ Please enter an HSF project directory"

    input_dir = Path(raw_path).expanduser()
    hsf_dir = _resolve_hsf_project_dir(input_dir)
    if not hsf_dir.exists():
        return False, f"❌ Directory does not exist: {hsf_dir}"
    if not hsf_dir.is_dir():
        return False, f"❌ Not a directory: {hsf_dir}"
    if not _looks_like_hsf_project(hsf_dir):
        candidates = _find_hsf_project_candidates(input_dir)
        if candidates:
            names = ", ".join(candidate.name for candidate in candidates[:8])
            suffix = "..." if len(candidates) > 8 else ""
            return False, f"❌ Multiple HSF projects found in directory; please select one: {names}{suffix}"
        return False, f"❌ Not a valid HSF project directory: {hsf_dir}"

    try:
        proj = load_project_from_disk_fn(str(hsf_dir))
    except Exception as e:
        return False, f"❌ Failed to load HSF project: {e}"

    msg = (
        f"✅ Loaded HSF project `{proj.name}` — {len(proj.parameters)} parameters, {len(proj.scripts)} scripts"
        f"\n\nSource directory: `{hsf_dir}`"
    )
    return finalize_loaded_project_fn(proj, msg, pending_gsm_name=proj.name, preserve_project_root=True)


def _resolve_hsf_project_dir(path: Path) -> Path:
    """Accept either an HSF root or a parent folder containing one HSF project."""
    if _looks_like_hsf_project(path):
        return path
    if not path.is_dir():
        return path

    candidates = _find_hsf_project_candidates(path)
    if len(candidates) == 1:
        return candidates[0]
    return path


def _find_hsf_project_candidates(path: Path) -> list[Path]:
    if not path.is_dir():
        return []
    return [child for child in sorted(path.iterdir()) if _looks_like_hsf_project(child)]


def _looks_like_hsf_project(path: Path) -> bool:
    return path.is_dir() and ((path / "libpartdata.xml").exists() or (path / "scripts").is_dir())


def handle_unified_import(
    uploaded_file,
    *,
    import_gsm_fn,
    parse_gdl_source_fn,
    derive_gsm_name_from_filename_fn,
    finalize_loaded_project_fn,
) -> tuple[bool, str]:
    fname = uploaded_file.name
    ext = Path(fname).suffix.lower()

    if ext == ".gsm":
        imported_project, msg = import_gsm_fn(uploaded_file.read(), fname)
        if not imported_project:
            detail = str(msg or "GSM import failed")
            if detail.startswith("❌"):
                return False, f"❌ [IMPORT_GSM] {detail[1:].strip()}"
            return False, f"❌ [IMPORT_GSM] {detail}"
        if isinstance(imported_project, (str, Path)):
            from openbrep.hsf_project import HSFProject

            proj = HSFProject.load_from_disk(str(imported_project))
        else:
            proj = imported_project
    else:
        try:
            content = uploaded_file.read().decode("utf-8", errors="replace")
            proj = parse_gdl_source_fn(content, Path(fname).stem)
        except Exception as e:
            return False, f"❌ Import failed: {e}"
        msg = f"✅ Imported GDL `{proj.name}` — {len(proj.parameters)} parameters, {len(proj.scripts)} scripts"

    import_gsm_name = derive_gsm_name_from_filename_fn(fname) or proj.name
    if ext == ".gsm":
        proj.save_to_disk()
    return finalize_loaded_project_fn(proj, msg, import_gsm_name)


def handle_open_path(
    source_path: str,
    *,
    normalize_pasted_path_fn,
    load_project_from_disk_fn,
    import_gsm_fn,
    parse_gdl_source_fn,
    derive_gsm_name_from_filename_fn,
    finalize_loaded_project_fn,
) -> tuple[bool, str]:
    raw_path = normalize_pasted_path_fn(source_path)
    if not raw_path:
        return False, "❌ Please select a file or HSF project directory to open"

    path = Path(raw_path).expanduser()
    if not path.exists():
        return False, f"❌ Path does not exist: {path}"

    if path.is_dir():
        return handle_hsf_directory_load(
            str(path),
            normalize_pasted_path_fn=normalize_pasted_path_fn,
            load_project_from_disk_fn=load_project_from_disk_fn,
            finalize_loaded_project_fn=finalize_loaded_project_fn,
        )

    if not path.is_file():
        return False, f"❌ Unsupported path type: {path}"

    ext = path.suffix.lower()
    if ext not in {".gdl", ".txt", ".gsm"}:
        return False, f"❌ Unsupported file type: {path.name}. Please select a .gdl, .txt, or .gsm file, or an HSF project directory."

    return handle_unified_import(
        _LocalPathUpload(path),
        import_gsm_fn=import_gsm_fn,
        parse_gdl_source_fn=parse_gdl_source_fn,
        derive_gsm_name_from_filename_fn=derive_gsm_name_from_filename_fn,
        finalize_loaded_project_fn=finalize_loaded_project_fn,
    )
