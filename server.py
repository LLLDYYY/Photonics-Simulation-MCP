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

KNOWLEDGE_DIR = Path("knowledge")


# ==========================================
# Helpers
# ==========================================

def load_yaml(filename: str):

    file_path = KNOWLEDGE_DIR / filename

    if not file_path.exists():

        return {}

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
                "match": keyword
            })

    return results


@mcp.tool()
def simulation_guard(
    software: str,
    version: str = ""
):
    """
    Return simulation warnings.

    Example:
    simulation_guard(
        software="lumerical",
        version="v241"
    )
    """

    software = software.lower()

    warnings = []

    if software == "lumerical":

        warnings.extend([

            {
                "id": "LUM001",
                "warning":
                "Negative X coordinates may cause hang."
            },

            {
                "id": "LUM002",
                "warning":
                "Avoid fdtd.run(); use FDTD engine."
            },

            {
                "id": "LUM003",
                "warning":
                "Use ASCII object names only."
            }
        ])

    elif software == "hfss":

        warnings.extend([

            {
                "id": "HFSS001",
                "warning":
                "Verify .asol file after solve."
            },

            {
                "id": "HFSS002",
                "warning":
                "Check radiation boundary."
            }
        ])

    return {
        "software": software,
        "version": version,
        "warnings": warnings
    }


# ==========================================
# Main
# ==========================================

if __name__ == "__main__":

    print(
        "Photonics Simulation Expert MCP Starting..."
    )

    mcp.run()