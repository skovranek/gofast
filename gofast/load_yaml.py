"""Module providing a function loading YAML."""
from typing import Any

from ruamel.yaml import YAML


# ruamel docs show Any type used for 'data' object
def load(yaml_file: str) -> Any:
    """Returns data from YAML file."""
    with open(yaml_file, 'r', encoding="utf-8") as yaml_data:
        yaml = YAML(typ="safe", pure=True)
        data = yaml.load(yaml_data)
    return data
