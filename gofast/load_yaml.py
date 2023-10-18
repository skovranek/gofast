from typing import Any

from ruamel.yaml import YAML

# ruamel docs show Any type used for 'data' object
def load(yaml_file: str) -> Any:
    with open(yaml_file, 'r') as yaml_data:
        try:
            yaml=YAML(typ="safe", pure=True)
            data = yaml.load(yaml_data)
        except yaml.YAMLError as e:
            print(f"YAML parsing error: {e}")

    return data
