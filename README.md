<p align="center">

<img src="assets/logo.png" width="1525" alt="logo">

</p>

# OpenBrep

## Quick Start

1. For regular users: Download `OpenBrep-*-macOS.zip` or `OpenBrep-*-Windows.zip` from [GitHub Releases](https://github.com/byewind1/openbrep/releases/latest)

2. After extraction, run `OpenBrep`

3. Command line / Developer users can then install using `git clone` or `pipx`

[Simplified Chinese](README.zh-CN.md) | English

**OpenBrep — An AI workbench for advanced ArchiCAD users and GDL developers. Compile and verify, knowledge-driven, asset traceable.** **

> **Code Your Boundaries**

> Official Release v0.6.12 — GDL Knowledge Base Calibration and Finalization: Completed official cross-validation of core commands, parameters, 2D/3D representations, and typical object archetypes, and solidified the commercialization skill direction at the Pro level.

---

## Problems and Solutions

You wrote some GDL code in AI and want to test it in ArchiCAD. Traditional path:

``` Open the Library Object Editor → Manually fill in parameters → Switch between 5 Script windows → Paste the code → Compile

```

**openbrep compresses this process to:**

``` Describe your requirements (Chinese/English are both acceptable) → AI generates and fills in the script box → One-click compilation → Drag the .gsm file into ArchiCAD

```

Or import an existing .gsm file and let AI help you debug, refactor, and add parameters.

---

## Installation and Launch

### Recommendation: Download the Desktop Package (for regular users)

Visit [GitHub Releases](https://github.com/byewind1/openbrep/releases/latest) and download the compressed package corresponding to your system:

- macOS: `OpenBrep-free-macOS.zip`

- Windows: `OpenBrep-free-Windows.zip`

Current macOS package compatibility: Apple Silicon only (`arm64`, M1/M2/M3/M4), macOS 14 Sonoma or later. Intel Mac is not covered by the current macOS zip.

On macOS, unzip it, open the `OpenBrep` folder, and double-click `OpenBrep.command`. On Windows, unzip it and run `OpenBrep.exe`. This path does not require users to learn `git clone`, `git pull`, or manual Python dependency installation first.

Temporary macOS Gatekeeper workaround:

The current macOS zip is not yet Developer ID signed and notarized. If macOS shows security warnings or blocks the app even after you confirm the prompts, remove the quarantine flag from the unzipped folder:

```bash
xattr -dr com.apple.quarantine /path/to/OpenBrep
```

Tip: type `xattr -dr com.apple.quarantine ` in Terminal, keep the trailing space, drag the unzipped `OpenBrep` folder into Terminal, then press Enter. After that, run `OpenBrep.command` again.

We are preparing a properly signed and notarized macOS package so this manual step will not be needed.

### Command line installation (advanced users)

OpenBrep is a Python application. After the official release to PyPI, it is recommended to install using an isolation tool:

```bash
pipx install "openbrep[ui]"
obr
```

Or use uv:

```bash
uv tool install "openbrep[ui]"
obr
```

### Source Code Installation (Developers)

```bash
git clone https://github.com/byewind1/openbrep.git
cd openbrep
bash install.sh
obr
```

> If `obr` is unavailable, reopen the terminal or run `source ~/.zshrc`

>
> `obr` by default only starts the UI locally at `http://localhost:8501` and will not automatically open a browser; please access it manually using your preferred browser or directly use the bookmarked address.


### Source Code Upgrade

```bash
cd openbrep
git pull origin main
bash install.sh # Rerun if new dependencies are added, harmless
obr
```

> Personal configuration (config.toml / API Key) remains unchanged after the upgrade, no reconfiguration required.

Requires Python 3.10+. Actual compilation (.gsm output) requires ArchiCAD 28/29.

---

## CLI Mode

Terminal workflow for GDL developers.

```bash
pip install -e "."

# Create an object
openbrep create "Make a bookshelf 600mm wide and 400mm deep with 4 shelves" --output ./my_shelf

# Modify an object (based on the HSF project directory on disk)
openbrep modify ./my_shelf "Change the number of shelves to 6, evenly spaced"

# View help
openbrep --help

```

Each modification reads the complete project state, precisely modifying rather than rewriting, and automatically compiles and verifies.

> Developer Note: If you are currently using `pip install -e "."` / `pip install -e ".[ui]"` for editable install, modifications to the repository source code will usually take effect immediately and do not require reinstallation; reinstallation is only recommended when changing `pyproject.toml`, dependencies, command entry points (such as `obr` / `obrcli`), or packaging rules.

` ... ---

## Feature Overview

### Editor Bar (Left Side)

| Feature | Description |

|---|---|

| 📂 **Import** | Drag and drop `.gdl` / `.txt` / `.gsm` files; .gsm files are unpacked into HSF using LP_XMLConverter |

| 🔧 **Compile GSM** | HSF → .gsm, supports Mock mode (no ArchiCAD required) and real LP_XMLConverter compilation |

| 📥 **Extract** | Scans code blocks from AI dialogues, automatically identifies script types (3D/2D/Param...) and writes them to the editor |

| **Script Tabs** | 6 independent script boxes (3D/2D/Master/Param/UI/Properties), each supporting streamlit-ace syntax highlighting and full-screen editing |

| **Parameter List** | View and manually add parameters; AI-generated paramlist.xml One-click writing |

| 🔍 **Syntax Check** | Matches IF/ENDIF, FOR/NEXT, ADD/DEL; 3D ends with END; 2D must have PROJECT2 |

### AI Dialogue Bar (Right Side)

| Function | Description |

|---|---|

| **🖼️ Image as Intent** | Upload building component image → AI recognizes geometry and extracts parametric dimensions → Directly generates GDL script, no text description required |

| **Natural Language Creation** | "Make a bookshelf 600mm wide and 400mm deep with 4 shelves" → Automatically generates all scripts and parameters |

| **Natural Language Modification** | When there is an existing project: "Change the number of shelves to 5, add a shelfMat parameter to the material" → AI understands the context and modifies as needed |

| **Debug Mode** | When containing words like "why"/"check"/"fix", automatically injects the entire script context; AI We can provide analysis text + code fixes |

| **Confirm Write** | AI modifications to existing projects will not be automatically overwritten; [✅ Write] [❌ Ignore] buttons will appear below the message |

| **Dialogue Operation Bar** | Below each AI message: 👍 👎 📋 🔄 (Positive/Negative/Copy/Regenerate) |

| **Multi-Model Support** | Local support for Claude / GLM / GPT / DeepSeek / Gemini / Ollama, switchable via sidebar |

---

## Supported LLMs

| Provider | Model | Description |

|---|---|---|

| Anthropic | claude-haiku / sonnet / opus | Recommended first choice |

| Zhipu | glm-5 / glm-4-flash | Available in China, high cost-performance ratio |

| OpenAI | gpt-4o / gpt-4o-mini / o3-mini | |

| DeepSeek | deepseek-chat / deepseek-reasoner | |

| Google | gemini-2.5-flash / pro | |

| Ollama | qwen2.5 / qwen3 / deepseek-coder | Local, no API Key required |

---

## GSM Import (AC29 Supported)

Select LP_XMLConverter mode in the sidebar. After configuring the path, you can import the .gsm file for modification:

```

# ArchiCAD 29 Path (LP_XMLConverter is embedded in the app bundle)

/Applications/GRAPHISOFT/Archicad 29/Archicad 29.app/Contents/MacOS/

LP_XMLConverter.app/Contents/MacOS/LP_XMLConverter

```

Alternatively, you can write the path directly in `config.toml`, which will be automatically read upon startup.

---

## Introduction to HSF Format

The directory structure (HSF) after uncompressing a .gsm file is as follows:

```
MyBookshelf/

├── libpartdata.xml ← Object identity (GUID, version)

├── paramlist.xml ← Parameter definition (strongly typed)

├── ancestry.xml ← Object category

└── scripts/

├── 1d.gdl ← Master Script

├── 2d.gdl ← 2D planar symbols

├── 3d.gdl ← 3D geometric model

├── vl.gdl ← Parameter logic (VALUES/LOCK)

└── ui.gdl ← Custom interface

```

openbrep uses HSF as its native format, each
Each script is processed independently; the AI ​​only reads scripts relevant to the current task (reducing context usage).

---

## Project Structure

The architecture specifications for maintainers and AI development tools can be found in:

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)

- [docs/AI_DEVELOPMENT_GUIDE.md](docs/AI_DEVELOPMENT_GUIDE.md)

- Chinese version: [docs/ARCHITECTURE.zh-CN.md](docs/ARCHITECTURE.zh-CN.md), [docs/AI_DEVELOPMENT_GUIDE.zh-CN.md](docs/AI_DEVELOPMENT_GUIDE.zh-CN.md)

```
openbrep/

├── openbrep/

│ ├── hsf_project.py # HSF data model

│ ├── paramlist_builder.py # Strongly typed generation of paramlist.xml

│ ├── gdl_parser.py # .gdl → HSFProject

│ ├── compiler.py # LP_XMLConverter wrapper

│ ├── core.py # Agent main loop + generate_only

│ ├── llm.py # Unified interface for multiple models

│ ├── knowledge.py # Knowledge base loading

│ └── skills_loader.py # Task strategy loading

├── ui/

│ └── app.py # Streamlit Web interface

├── knowledge/ # GDL reference documentation (can be expanded)

├── skills/ # Task strategy (can be expanded)

├── docs/

│ └── manual.md # Detailed user manual

├── tests/ # Unit tests

├── config.example.toml

└── pyproject.toml

```

---

## Configuration

Copy `config.example.toml` should be replaced with `config.toml` (already defined in .gitignore). Fill in the information as needed.

### 1) Official provider (`provider_keys`)

```toml
[llm]
model = "glm-4-flash"
temperature=0.2
max_tokens = 4096

[llm.provider_keys]
zhipu = "your-zhipu-key"
anthropic = "your-claude-key"
openai = "your-openai-key"
deepseek = "your-deepseek-key"
google = "your-gemini-key"
aliyun = "your-qwen-key"
kimi = "your-kimi-key"
```

Prefix matching rules:
- `glm-` → `zhipu`
- `deepseek-` → `deepseek`
- `claude-` → `anthropic`
- `gemini-` → `google`
- `qwen-` / `qwq-` → `aliyun`

- `moonshot-` → `kimi`

- `gpt-` / `o1` / `o3` / `o4` → `openai`

- `ollama/` → Local mode, no API Key required

### 2) Custom provider (recommended object syntax)

```toml

[llm]

model = "ymg-gpt-5.3-codex"

api_key = "YOUR_YMG_KEY"

api_base = "https://api.ymg.com/v1"

[[llm.custom_providers]]

name = "ymg"

protocol = "openai" # openai | anthropic

base_url = "https://api.ymg.com/v1"

api_key = "YOUR_YMG_KEY"

[[llm.custom_providers.models]]

alias = "ymg-gpt-5.3-codex" # The name selected in the UI

model = "gpt-5.3-codex" # The actual model name requested to the provider

```

### 3) Route Priority (Important)

The parsing order of models and credentials during requests:

1. `custom_providers` (first matched by alias/model)

2. `provider_keys` (matched by model prefix)

3. `[llm]` Top-level `api_key` / `api_base` (fallback)

That is to say: when a custom provider is matched, the provider's `api_key/base_url/protocol` will be used first.

### 4) Common Pitfalls

- Writing only `models = ["ymg-gpt-5.3-codex"]` without writing the `{alias, model}` object can easily cause confusion between the alias and the actual model name.

- `base_url` is not an OpenAI compatible entry point (commonly, `/v1` is missing).

- After switching models, it was not confirmed whether `[llm].model/api_key/api_base` is consistent with the current provider group.

### 5) Compiler

```toml

[compiler]

path = "/Applications/GRAPHISOFT/Archicad 29/.../LP_XMLConverter"

```

---

## Documentation

- **[User Manual →](docs/manual.md)** — Detailed descriptions, workflows, and frequently asked questions for each UI feature

---

## Version History

| Version | Main Content |

|---|---|

| v0.6.12 | GDL Knowledge Base Calibration and Finalization: Completed cross-validation of official documentation/community/local knowledge for batches P0-P6, corrected core command semantics, parameter structure, 2D/3D projection and advanced geometric boundaries, and supplemented the Pro layer commercial Skill development direction (see docs/releases/v0.6.12.md) |

| v0.6.11 | macOS Installer Fixes: Added Streamlit Frozen front-end static resources and hidden imports of `streamlit.runtime.scriptrunner` in the package; added a browser-level package verification script to ensure that not only health passes, but also homepage and script execution pass (see docs/releases/v0.6.11.md) |

| v0.6.10 | macOS Installer Fixes: The packaging launcher explicitly disables Streamlit `global.developmentMode` to avoid `server.port` conflicts; retains the package-level smoke verification entry point for direct verification of the Release zip (see docs/releases/v0.6.10.md) |

| v0.6.9 | Installer Verification Patch: The packaging launcher supports fixed ports and disabling automatic browser opening; added `scripts/package_smoke.py` for directly running the in-package launcher and verifying Streamlit health after downloading the Release zip, without relying on local `obr` (see docs/releases/v0.6.9.md) |

| v0.6.8 | macOS Package Fixes: The packaging launcher is now launched in-process using Streamlit to avoid recursively restarting frozen packages; macOS zip adds `OpenBrep.command` and startup instructions; `openbrep[ui]` explicitly includes dependencies required for UI import (see docs/releases/v0.6.8.md) |

| v0.6.7 | UI Finalization: Hides the version management and Archicad integration entry points, streamlines HSF save/save as actions, cleans up unnecessary prompts and low-frequency operations, further reducing the cognitive load on the workbench (see docs/releases/v0.6.7.md) |

| v0.6.6 | UI Cleanup: Split the open file/HSF project entry points, simplifies GSM compilation and output directory selection, removes low-value debug buttons and redundant prompts, and optimizes the macOS native file selector activation experience (see docs/releases/v0.6.6.md) |

| v0.6.5 | Installation Experience Patch: Fixed the GitHub Release automatic release command, replacing it with `gh release create --generate-notes` for compatibility with `--repo`, to continue the package release automation from v0.6.4 (see docs/releases/v0.6.5.md) |

| v0.6.4 | Minor Installation Experience Version: GitHub Release desktop packages are now the preferred choice for regular users; fixed the macOS/Windows installer workflow artifact path and automatically creates/updates GitHub Releases after tag builds; added instructions for layered installation using pipx/uv/git clone (see docs/releases/v0.6.4.md) |

| v0.6.3 | Added personal workspace memory: persistent chat logs, GDL error log, and user-triggered self-improvement skills; LLM injection layered for user workspace memory and source code developer baseline; optimized HSF project directory persistence, build version recognition, custom provider configuration synchronization, parameter unit documentation, and UI architecture governance (see... (docs/releases/v0.6.3.md) |

| v0.6.2 | Added wiki knowledge retrieval and Q&A links; added user-defined flat knowledge base access; added conversational creation and list routing for skill creator; completed pipeline/knowledge/skill related tests and fixed key chat routing details (see docs/releases/v0.6.2.md) |

| v0.6.1 | Improved CLI usability and installation experience; added/improved GDL static checks and automatic repair; strengthened chat/explainer/image links and reference diagram generation; fixed the issue of OBR failing to start the UI in non-project directories (see docs/releases/v0.6.1.md) |

| v0.6.0 | Runtime Phase 1 main framework officially released and finalized: unified create/modify/repair/chat main links; repair independent intent closure; unified CLI/UI/runtime versions and release guidelines (see docs/releases/v0.6.1.md) (docs/releases/v0.6.0.md) |

| v0.5.7 | CLI mode is now officially available (create/modify commands); the build process supports user cancellation; pipeline improvements address the issue of progressively worsening performance; parameter routing is fixed (see docs/releases/v0.5.7.md) |

| v0.5.6 | Image uploads no longer freeze; false alarms from cross-script/static checkers are reduced; AI assistant settings support long-term storage and injection of system prompts; custom proxy and official vendor layered selection, with priority given to proxy names (see docs/releases/v0.5.6.md) |

| v0.5.5 | UI refactored to a four-column layout: left column for operations + preview, middle column for scripts + parameter table, right column for AI dialogue (see docs/releases/v0.5.5.md) |

| v0.5.4 | Validator layered refactoring: error/warning separated, hard error whitelist tightened; cross-script checker; debug Minimal changes; real-time display of the build process; widgets disabled during build.
(See docs/releases/v0.5.4.md) | | **v0.5.3** | Knowledge base upgrade and document brand enhancement: Integrate book breakdown increments (including 2D advanced and compilable examples), add command index and command-level precise routing, and add a logo to the top of the README (see `docs/releases/v0.5.3.md`). | | **v0.5.2** | Version labeling and release archiving standardization: UI version number uniformly reads code version; README title removes version; Added release notes (see `docs/releases/v0.5.2.md`) |

| **v0.5.1** | Package release preparation: Added macOS/Windows packaging script and GitHub Actions build process (PyInstaller) |

| **v0.5** | **OpenBrep brand launch** — Project renamed OpenBrep; Stable version release; Gitee mirror support (fast access for domestic users) |

| v0.5 pre | Unified editor UI; **Image as Intent** (upload image → AI generates GDL); AI dialogue script modification; Confirmation writing process; Automatic injection of paramlist.xml; GSM import (AC29); Streamlit-ace syntax highlighting; Full-screen editing; Multi-model support |

| v0.4.0 | HSF-native architecture refactoring; Streamlit Web UI; Strong typing paramlist; 44 unit tests |

| v0.3.x | GDL parser; Context surgery; Preflight |

| v0.2.0 | Anti-hallucination; Golden snippets |

| v0.1.0 | Core agent loop |

---

## License

MIT — see [LICENSE](LICENSE).
