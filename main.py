import yaml

with open('data.yml', 'r') as yaml_data:
    try:
        data = yaml.load(yaml_data, Loader=yaml.FullLoader)
    except yaml.YAMLError as e:
        print(f"YAML parsing error: {e}")

print(data['key'])
