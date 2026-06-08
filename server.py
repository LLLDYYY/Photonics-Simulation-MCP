from pathlib import Path
import yaml

from mcp.server.fastmcp import FastMCP

# ==========================================
# MCP Server
# ==========================================

mcp = FastMCP(
    "Photonics Simulation Expert"
)

# ==========================================
# Knowledge Directory
# ==========================================

KNOWLEDGE_DIR = Path(__file__).parent / "knowledge"


# ==========================================
# Helpers
# ==========================================

def load_yaml(filename: str):

    file_path = KNOWLEDGE_DIR / filename

    if not file_path.exists():

        return {"_load_error": f"File not found: {filename}"}

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as f:

        return yaml.safe_load(f)


def load_all_knowledge():

    data = {}

    for file in KNOWLEDGE_DIR.glob("*.yaml"):

        try:

            with open(
                file,
                "r",
                encoding="utf-8"
            ) as f:

                data[file.name] = yaml.safe_load(f)

        except Exception as e:

            data[file.name] = {
                "error": str(e)
            }

    return data


# ==========================================
# MCP Tools
# ==========================================

@mcp.tool()
def hello():
    """
    Health check.
    """

    return {
        "status": "ok",
        "server": "Photonics Simulation Expert MCP"
    }

@mcp.tool()
def get_rule(rule_id: str):
    """
    Retrieve a specific rule or bug by its ID across all knowledge files.
    Examples: "LUM001", "HFSS001", "COMSOL002"
    """
    rule_id = rule_id.upper()
    for file in KNOWLEDGE_DIR.glob("*.yaml"):
        data = load_yaml(file.name)
        for list_key in ("bugs", "rules", "physics"):
            items = data.get(list_key, [])
            if not isinstance(items, list):
                continue
            for item in items:
                if item.get("id", "").upper() == rule_id:
                    return {"found": True, "source": file.name, "data": item}
    return {"found": False, "message": f"Rule {rule_id} not found"}

@mcp.tool() 
def list_knowledge_files():
    """
    List all available knowledge files.
    """

    return sorted([
        file.name
        for file in KNOWLEDGE_DIR.glob("*.yaml")
    ])


@mcp.tool()
def get_lumerical_bugs():
    """
    Return Lumerical bug database.
    """

    return load_yaml(
        "lumerical_bugs.yaml"
    )


@mcp.tool()
def get_hfss_bugs():
    """
    Return HFSS bug database.
    """

    return load_yaml(
        "hfss_bugs.yaml"
    )

@mcp.tool()
def get_comsol_rules():
    """
    Return COMSOL rules.
    """

    return load_yaml(
        "comsol_rules.yaml"
    )


@mcp.tool()
def get_pyaedt_rules():
    """
    Return PyAEDT rules.
    """

    return load_yaml(
        "pyaedt_rules.yaml"
    )


@mcp.tool()
def get_physics_rules():
    """
    Return photonics physics rules.
    """

    return load_yaml(
        "physics_rules.yaml"
    )


@mcp.tool()
def get_checklists():
    """
    Return simulation checklists.
    """

    return load_yaml(
        "simulation_checklists.yaml"
    )


@mcp.tool()
def get_all_knowledge():
    """
    Return all loaded knowledge.
    """

    return load_all_knowledge()

@mcp.tool()
def get_workflow(
    workflow_name: str
):
    """
    Return workflow steps.

    Examples:
    - fdtd
    - hfss
    """

    data = load_yaml(
        "workflows.yaml"
    )

    workflows = data.get(
        "workflows",
        {}
    )

    return workflows.get(
        workflow_name,
        []
    )


@mcp.tool()
def search_knowledge(
    keyword: str
):
    """
    Search all knowledge files.

    Example:
    search_knowledge("hang")
    """

    keyword = keyword.lower()

    results = []

    for file in KNOWLEDGE_DIR.glob("*.yaml"):

        text = file.read_text(
            encoding="utf-8"
        )

        if keyword in text.lower():

            results.append({
                "file": file.name,
                "content": text[:1000]
            })

    return results

@mcp.tool()
def get_lumerical_api_rules():

    return load_yaml(
        "lumerical_api_rules.yaml"
    )

@mcp.tool()
def simulation_guard(
    software: str
):
    """
    Return known warnings
    for selected software.
    """

    software = software.lower()

    warnings = []

    if software == "lumerical":

        data = load_yaml(
            "lumerical_bugs.yaml"
        )

        warnings.extend(
            data.get(
                "bugs",
                []
            )
        )

    elif software == "hfss":

        for key in ("hfss_bugs.yaml", "hfss_rules.yaml", "pyaedt_rules.yaml"):
            data = load_yaml(key)
        for list_key in ("bugs", "rules"):

            warnings.extend(
            data.get(
                "rules",
                []
            )
        )

    elif software == "comsol":

        data = load_yaml(
            "comsol_rules.yaml"
        )

        warnings.extend(
            data.get(
                "rules",
                []
            )
        )

    return {
        "software": software,
        "warnings": warnings
    }

@mcp.tool()
def get_tool_recommendation(
    task: str
):
    """
    Recommend simulation tool.

    Examples:
    mode_analysis
    directional_coupler
    microwave_cpw
    fullwave_3d
    electro_optic_modulator
    """

    mapping = {

        "mode_analysis": {
            "tool": "Lumerical FDE",
            "reason":
            "fast and accurate"
        },

        "directional_coupler": {
            "tool":
            "FDE Supermode + CMT",
            "reason":
            "much faster than FDTD"
        },

        "microwave_cpw": {
            "tool":
            "COMSOL 2D FEM",
            "reason":
            "literature standard"
        },

        "fullwave_3d": {
            "tool":
            "HFSS",
            "reason":
            "high accuracy"
        },

        "electro_optic_modulator": {
            "tool":
            "FDE + overlap integral",
            "reason":
            "avoid expensive full-wave simulation"
        }
    }

    return mapping.get(
        task,
        {}
    )

@mcp.tool()
def get_checklist(
    checklist_name: str
):
    """
    Return simulation checklist.
    """

    data = load_yaml(
        "simulation_checklists.yaml"
    )

    checklists = data.get(
        "checklists",
        {}
    )

    return checklists.get(
        checklist_name,
        []
    )

# ==========================================
# Main
# ==========================================

if __name__ == "__main__":

    print(
        "Photonics Simulation Expert MCP Starting..."
    )

    mcp.run()