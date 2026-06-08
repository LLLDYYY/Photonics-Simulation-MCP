import yaml

with open(
    "knowledge/lumerical_bugs.yaml",
    "r",
    encoding="utf-8"
) as f:

    data = yaml.safe_load(f)

print(data)