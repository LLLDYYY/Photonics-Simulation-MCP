# Photonics Simulation MCP

Knowledge-based MCP server for photonics simulation engineering.

Supported software: Lumerical FDTD/MODE/FDE, HFSS, COMSOL, PyAEDT.

## Knowledge Base

All knowledge is stored in the knowledge/ directory as structured YAML files:

- lumerical_bugs.yaml — Lumerical FDTD/MODE known bugs and workarounds
- lumerical_api_rules.yaml — API function names, parameters, and encoding rules
- hfss_bugs.yaml — HFSS BatchSolve and boundary issues
- hfss_rules.yaml — .aedt file format, port naming, and setup syntax
- comsol_rules.yaml — COMSOL MPh API and mode analysis rules
- pyaedt_rules.yaml — PyAEDT import paths and compatibility
- physics_rules.yaml — Anisotropy, conductivity, unit conversion, 2D/3D differences
- simulation_checklists.yaml — Pre-run checklists and general engineering principles
- workflows.yaml — Tool selection guide and step-by-step workflows

## Installation

Clone repository and install dependencies:

    git clone https://github.com/LLLDYYY/Photonics-Simulation-MCP.git
    cd Photonics-Simulation-MCP
    python -m pip install -r requirements.txt

Start the MCP server:

    python server.py

## Available Tools

### Query and Search

- hello() — Health check
- get_rule(rule_id) — Retrieve a specific rule by ID (e.g., LUM001, HFSS004, PHY008)
- search_knowledge(keyword) — Full-text search across all knowledge files
- list_knowledge_files() — List all available YAML knowledge files
- get_all_knowledge() — Load and return the entire knowledge base

### Software-Specific

- get_lumerical_bugs() — Lumerical bug database
- get_lumerical_api_rules() — Lumerical API naming and syntax rules
- get_hfss_bugs() — HFSS bug database
- get_comsol_rules() — COMSOL rules and API guidelines
- get_pyaedt_rules() — PyAEDT compatibility and import rules
- get_physics_rules() — Physics rules (anisotropy, conductivity, unit conversion)

### Guard and Checklists

- simulation_guard(software) — Return all known warnings for a given software (lumerical, hfss, or comsol)
- get_checklist(name) — Return pre-run checklists (e.g., lumerical_before_run, hfss_before_solve, general_principles)
- get_workflow(name) — Return workflow steps (e.g., fdtd, hfss, tool_selection)
- get_tool_recommendation(task) — Recommend simulation tool for a task

## Tool Recommendation Examples

Task: mode_analysis -&gt; Tool: Lumerical FDE (Fast, high accuracy, good anisotropy support)

Task: directional_coupler -&gt; Tool: FDE Supermode + CMT (Much faster than FDTD, sufficient accuracy)

Task: microwave_cpw -&gt; Tool: COMSOL 2D FEM (2D cross-section sufficient, literature standard)

Task: fullwave_3d -&gt; Tool: HFSS (Mature, high accuracy, but .aedt format has many pitfalls)

Task: electro_optic_modulator -&gt; Tool: FDE + overlap integral (No full-wave simulation needed)

## Cursor MCP Configuration

Add to your Cursor MCP settings:

    {
      "mcpServers": {
        "photonics": {
          "command": "python",
          "args": [
            "/absolute/path/to/Photonics-Simulation-MCP/server.py"
          ]
        }
      }
    }

Note: Use the absolute path to server.py to ensure the knowledge directory is resolved correctly.

## Repository

https://github.com/LLLDYYY/Photonics-Simulation-MCP