# Photonics Simulation MCP

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Knowledge-based MCP server for photonics simulation engineering.

Supported software:

- Lumerical FDTD
- HFSS
- COMSOL

Current capabilities:

- Known bug database
- Engineering experience repository
- Workflow guidance

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

### `hello()`

Returns MCP health status.

### `get_lumerical_bugs()`

Returns known Lumerical issues.

### `get_hfss_bugs()`

Returns known HFSS issues.

### `get_comsol_rules()`

Returns COMSOL simulation rules.

### `get_pyaedt_rules()`

Returns PyAEDT usage rules.

### `get_physics_rules()`

Returns photonics physics rules.

### `get_simulation_guard(software)`

Returns known warnings for selected software.

### `get_tool_recommendation(task)`

Recommends simulation tool based on task.

### `get_workflow(workflow_name)`

Returns workflow steps.

### `search_knowledge(keyword)`

Search all knowledge files.

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

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Repository

https://github.com/LLLDYYY/Photonics-Simulation-MCP
