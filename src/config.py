import pathlib
import yaml

# The config file gets read and parsed here.


conf_file_path = pathlib.Path(__file__).parent / "config.yaml"

if conf_file_path.exists() is False:
    raise FileNotFoundError("Config file (config.yaml) not found.")


with open(conf_file_path, "r", encoding= "utf-8") as file:
    config = yaml.safe_load(file.read())


user_agent = f"{config["name"]}:{config["version"]} (by u/{config["main_acc"]}) {config["additional_info"]}"
