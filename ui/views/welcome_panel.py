from __future__ import annotations

from typing import Callable


def render_welcome(
    st,
    *,
    browse_and_open_project_file_fn: Callable[[], tuple[bool, str]] | None = None,
    browse_and_load_hsf_directory_fn: Callable[[], tuple[bool, str]] | None = None,
) -> None:
    st.markdown(
        """
<div class="welcome-card">
<h2 style="color:#22d3ee; margin-top:0; font-family:'JetBrains Mono';">Welcome to OpenBrep 🏗️</h2>
<p style="color:#94a3b8;">Drive ArchiCAD GDL object creation and compilation with natural language. No GDL syntax knowledge required — just describe what you need.</p>
</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown("#### Quick Start in Three Steps")
    st.info("**① Configure API Key**  \nSelect an AI model in the left sidebar and enter the corresponding API Key. The free ZhipuAI GLM model can be used directly.")
    st.info("**② Start a Conversation**  \nDescribe the GDL object you want to create in the input box at the bottom, for example:  \n\"Create a bookshelf 600 mm wide and 400 mm deep, with an iShelves parameter to control the number of shelves\"")
    st.info("**③ Compile Output**  \nThe AI generates code and automatically triggers compilation. Real compilation requires configuring the LP_XMLConverter path in the sidebar. Mock mode validates the structure without installing ArchiCAD.")

    st.divider()
    st.markdown("#### Or: Open an Existing Project / File")
    if browse_and_open_project_file_fn is not None:
        if st.button(
            "📄 Open File",
            key="welcome_open_project_file",
            width="stretch",
            help="Supports .gdl / .txt / .gsm files",
        ):
            ok, msg = browse_and_open_project_file_fn()
            if ok:
                st.rerun()
            elif msg.startswith("❌"):
                st.error(msg)
            elif msg:
                st.info(msg)

    if browse_and_load_hsf_directory_fn is not None:
        if st.button(
            "📂 Open HSF Project",
            key="welcome_open_hsf_project",
            width="stretch",
            help="Select an HSF project directory",
        ):
            ok, msg = browse_and_load_hsf_directory_fn()
            if ok:
                st.rerun()
            elif msg.startswith("❌"):
                st.error(msg)
            elif msg:
                st.info(msg)

    st.divider()
    st.caption("💡 Tip: No need to create a project for your first message — just describe what you need and the AI will initialize one automatically.")
