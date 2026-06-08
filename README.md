# Photonics Simulation MCP

Knowledge-based MCP server for photonics simulation engineering.

Supported software:

* Lumerical FDTD
* HFSS
* COMSOL

Current capabilities:

* Known bug database
* Engineering experience repository
* Workflow guidance

## Installation

### Clone repository

```bash
git clone https://github.com/LLLDYYY/Photonics-Simulation-MCP.git
cd Photonics-Simulation-MCP
```

### Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Start MCP Server

```bash
python server.py
```

## Available Tools

### get_lumerical_bugs()

Returns known Lumerical issues.

### get_hfss_bugs()

Returns known HFSS issues.

### hello()

Returns MCP health status.

## Cursor MCP Configuration

Example:

```json
{
  "mcpServers": {
    "photonics": {
      "command": "python",
      "args": [
        "server.py"
      ]
    }
  }
}
```

## Repository

https://github.com/LLLDYYY/Photonics-Simulation-MCP
