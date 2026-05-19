from __future__ import annotations

from typing import Callable

from openbrep.hsf_project import GDLParameter, HSFProject
from openbrep.paramlist_builder import build_paramlist_xml, clean_parameter_description, validate_paramlist


def render_parameter_panel(
    st,
    proj: HSFProject,
    *,
    render_tapir_inspector_fn: Callable[[], None] | None = None,
    render_tapir_param_workbench_fn: Callable[[], None] | None = None,
) -> None:
    st.markdown("### Object Parameters")
    _render_project_parameters(st, proj)
    if render_tapir_inspector_fn is not None and render_tapir_param_workbench_fn is not None:
        _render_archicad_parameter_bridge(
            st,
            render_tapir_inspector_fn=render_tapir_inspector_fn,
            render_tapir_param_workbench_fn=render_tapir_param_workbench_fn,
        )


def _render_project_parameters(st, proj: HSFProject) -> None:
    editable_count = sum(1 for param in proj.parameters if not param.is_fixed)
    fixed_count = len(proj.parameters) - editable_count
    count_col, editable_col, fixed_col = st.columns(3)
    count_col.metric("Total Parameters", len(proj.parameters))
    editable_col.metric("Editable", editable_count)
    fixed_col.metric("Fixed", fixed_count)

    with st.expander("Parameter Info"):
        st.markdown(
            "**Parameter List** — Adjustable parameters of the GDL object.\n\n"
            "- **Type**: `Length` / `Integer` / `Boolean` / `Material` / `String`\n"
            "- **Name**: Variable name referenced in code (camelCase, e.g. `iShelves`)\n"
            "- **Value**: Default value\n"
            "- **Fixed**: When checked, the user cannot modify this in ArchiCAD"
        )

    param_data = [
        {
            "Type": param.type_tag,
            "Variable Name": param.name,
            "Default Value": param.value,
            "Description": clean_parameter_description(param.description, param.type_tag),
            "Fixed": "Yes" if param.is_fixed else "",
        }
        for param in proj.parameters
    ]
    if param_data:
        st.dataframe(param_data, width="stretch", hide_index=True)
    else:
        st.caption("No parameters yet. Add them via AI conversation or manually.")

    _render_manual_parameter_form(st, proj)
    _render_parameter_validation(st, proj)

    with st.expander("paramlist.xml Preview"):
        st.code(build_paramlist_xml(proj.parameters), language="xml")


def _render_archicad_parameter_bridge(
    st,
    *,
    render_tapir_inspector_fn: Callable[[], None] | None,
    render_tapir_param_workbench_fn: Callable[[], None] | None,
) -> None:
    if render_tapir_inspector_fn is None or render_tapir_param_workbench_fn is None:
        st.info("Archicad parameter write-back is not enabled.")
        return

    st.caption("Read the currently selected object from Archicad, inspect the object info, then edit parameters and write them back.")
    inspect_tab, edit_tab = st.tabs(["Selected Object", "Parameter Edit"])
    with inspect_tab:
        render_tapir_inspector_fn()
    with edit_tab:
        render_tapir_param_workbench_fn()


def _render_manual_parameter_form(st, proj: HSFProject) -> None:
    with st.expander("➕ Add Parameter Manually"):
        type_col, name_col, value_col, desc_col = st.columns(4)
        with type_col:
            param_type = st.selectbox(
                "Type",
                [
                    "Length",
                    "Integer",
                    "Boolean",
                    "RealNum",
                    "Angle",
                    "String",
                    "Material",
                    "FillPattern",
                    "LineType",
                    "PenColor",
                ],
            )
        with name_col:
            param_name = st.text_input("Variable Name", value="bNewParam")
        with value_col:
            param_value = st.text_input("Default Value", value="0")
        with desc_col:
            param_desc = st.text_input("Description")

        if st.button("Add Parameter"):
            try:
                proj.add_parameter(GDLParameter(param_name, param_type, param_desc, param_value))
                st.success(f"✅ {param_type} {param_name}")
                st.rerun()
            except Exception as exc:
                st.error(str(exc))


def _render_parameter_validation(st, proj: HSFProject) -> None:
    if not st.button("🔍 Validate Parameters"):
        return

    issues = validate_paramlist(proj.parameters)
    for issue in issues:
        st.warning(issue)
    if not issues:
        st.success("✅ Parameter validation passed")
