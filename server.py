from pathlib import Path
import yaml

from mcp.server.fastmcp import FastMCP

# 创建MCP服务
mcp = FastMCP(
    "Photonics Simulation Expert"
)

# 知识库目录
KNOWLEDGE_DIR = Path("knowledge")


def load_yaml(filename):
    """读取yaml文件"""

    with open(
        KNOWLEDGE_DIR / filename,
        "r",
        encoding="utf-8"
    ) as f:

        return yaml.safe_load(f)


@mcp.tool()
def get_lumerical_bugs():
    """
    Get known Lumerical bugs.
    """

    return load_yaml(
        "lumerical_bugs.yaml"
    )

@mcp.tool()
def get_hfss_bugs():
    """
    Get known HFSS bugs.
    """

    return load_yaml(
        "hfss_bugs.yaml"
    )

@mcp.tool()
def hello():
    """
    Test MCP connection.
    """

    return {
        "message":
        "Photonics MCP is running correctly!"
    }


if __name__ == "__main__":

    print(
        "Photonics MCP Server Starting..."
    )

    mcp.run()