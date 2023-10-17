#!/usr/bin/env python

import sys
from ruamel.yaml import YAML

with open(sys.argv[1], 'r') as yaml_data:
    try:
        yaml=YAML(typ="safe", pure=True)
        data = yaml.load(yaml_data)
    except yaml.YAMLError as e:
        print(f"YAML parsing error: {e}")

print(data['key'])

with open(sys.argv[2], 'a') as f:
    f.write(data['key'])
