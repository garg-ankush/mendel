import yaml


def read_configs():
    with open("/Users/ankushgarg/Desktop/projects/mendel/config.yaml", "r") as stream:
        try:
            config_file = yaml.safe_load(stream)
            flattened_configs = {}
            for key, value in config_file.items():
                if isinstance(value, dict):
                    for k, v in value.items():
                        flattened_configs[k] = v
                else:
                    flattened_configs[key] = value

        except yaml.YAMLError as exc:
            print(exc)
    return flattened_configs
