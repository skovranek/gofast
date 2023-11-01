from typing import Any

from ruamel.yaml import YAML

# ruamel docs show Any type used for 'data' object
def load(yaml_file: str) -> Any:
    with open(yaml_file, 'r') as yaml_data:
        yaml = YAML(typ="safe", pure=True)
        data = yaml.load(yaml_data)
    return data
