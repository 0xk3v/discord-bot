import json


config_path = "config/config.json"

with open(config_path) as f:
    try:
        config_json = json.loads(f.read())
    except Exception as e:
        print(str(e))


def get_config(key):
    return config_json[key]
