from __future__ import annotations

from typing import Callable


VISION_SYSTEM_PROMPT = """\
You are a professional GDL architect with expert knowledge of ArchiCAD GDL scripting (GDL Reference v26 standard).
The user has uploaded an image of an architectural component, furniture, or fixture. Please output the following structure:

## Component Identification
- Type: (bookshelf / table/chair / door/window / staircase / column / wall panel / lighting fixture / ...)
- Geometry: (primary shape, structural hierarchy, detail features — 2–4 sentences)
- Material/Surface: (visible materials, for use as Material parameter default values)

## Parametric Analysis
List all parametrizable dimensions in GDL paramlist format. Architectural dimensions may be estimated in mm, but must be converted to m when writing the paramlist:

```
Length w  = 0.9     ! total width
Length h  = 2.1     ! total height
Length d  = 0.3     ! total depth
Integer n = 4       ! number of repeated units
Material mat = "Wood"  ! primary material
```

## GDL 3D Script

```gdl
! [component name] — AI generated from image
! Parameters: w h d n mat

MATERIAL mat

! main body
BLOCK w, d, h

END
```

Rules:
- The paramlist code block must contain ≥2 lines in `Type Name = value  ! comment` format
- Length parameter values must use m; do not include unit annotations (mm/m/metres/millimetres etc.) in parameter names or comments
- The last line of the 3D Script must be `END` (on its own line)
- All dimensions must be parameter-driven; hardcoded numbers are not allowed
- GDL commands must be fully uppercase (BLOCK / CYLIND / LINE3 / ADD / DEL / FOR / NEXT etc.)
- Use FOR/NEXT loops for repeated elements (shelves / grilles / louvres)
"""


def run_vision_generate(
    *,
    image_b64: str,
    image_mime: str,
    extra_text: str,
    proj,
    status_col,
    auto_apply: bool,
    session_state,
    logger,
    get_llm_fn: Callable[[], object],
    begin_generation_state_fn: Callable[[object], str],
    guarded_event_update_fn: Callable[[object, str, str, str], None],
    consume_generation_result_fn: Callable[[str], bool],
    finalize_generation_fn: Callable[[str, str], bool],
    generation_cancelled_message_fn: Callable[[], str],
    classify_code_blocks_fn: Callable[[str], dict],
    apply_generation_result_fn: Callable[[dict, object, str | None, bool], tuple[str, list[str]]],
    classify_vision_error_fn: Callable[[Exception], str],
    error_fn: Callable[[str], None],
) -> str:
    generation_id = begin_generation_state_fn(session_state)
    status_ph = status_col.empty()
    try:
        llm = get_llm_fn()
        logger.info(
            "vision generate start route=generate image_mime=%s has_project=%s prompt_len=%d",
            image_mime,
            bool(proj),
            len(extra_text or ""),
        )
        guarded_event_update_fn(status_ph, generation_id, "info", "🖼️ AI is analyzing the image...")

        user_text = extra_text.strip() if extra_text else "Please analyze this image and generate the corresponding GDL script."
        resp = llm.generate_with_image(
            text_prompt=user_text,
            image_b64=image_b64,
            image_mime=image_mime,
            system_prompt=VISION_SYSTEM_PROMPT,
        )
        if not consume_generation_result_fn(generation_id):
            status_ph.empty()
            finalize_generation_fn(generation_id, "cancelled")
            return generation_cancelled_message_fn()

        status_ph.empty()
        raw_text = resp.content
        extracted = classify_code_blocks_fn(raw_text)

        if extracted:
            result_prefix, _ = apply_generation_result_fn(extracted, proj, None, auto_apply)
            finalize_generation_fn(generation_id, "completed")
            return result_prefix + raw_text

        finalize_generation_fn(generation_id, "completed")
        return f"🖼️ **Image analysis complete** (no GDL code blocks detected — AI may have provided a text-only analysis)\n\n{raw_text}"

    except Exception as exc:
        status_ph.empty()
        finalize_generation_fn(generation_id, "failed")
        logger.warning("vision generate failed error=%s", exc.__class__.__name__)
        err_msg = classify_vision_error_fn(exc)
        error_fn(err_msg)
        return f"❌ {err_msg}"
