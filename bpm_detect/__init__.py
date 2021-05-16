"""get some variables going"""
from configparser import ConfigParser
from pathlib import Path
import appdirs
from bpm_detect.get_downloads_dir import get_downloads_dir


def create_dir(directory: Path):
    """create a directory if it doesn't exist"""
    try:
        if not directory.exists():
            directory.mkdir(parents=True)
    except PermissionError as err:
        print(f"PermissionError: Unable to create {directory}.\nExiting.")
        raise SystemExit from err
    else:
        print(f"Created directory '{directory}'")


def read_config(configfile: Path):
    """read a config file"""
    if not configfile.exists():
        write_config(configfile)
    config: ConfigParser = ConfigParser()
    raise NotImplementedError


def write_config(configfile: Path):
    """write a configuration file"""
    config: ConfigParser = ConfigParser()
    placeholder_text: str = "Replace this with your {}"

    config["PATHS"] = {"Download Directory": str(DIRECTORIES["DOWNLOAD_BASE_PATH"])}
    config["TOKENS"] = {
        "Client ID": placeholder_text.format("Client ID"),
        "Client Secret": placeholder_text.format("Client Secret"),
        "User ID": placeholder_text.format("User ID [optional]"),
    }

    with configfile.open("w") as file:
        config.write(file)


NAME: str = "bpm_detector"

# TODO (jam) config file for these locations
DIRECTORIES: dict[str, Path] = {
    "CONFIG_DIR": Path(appdirs.user_config_dir(NAME)),
    "DOWNLOAD_BASE_PATH": Path(get_downloads_dir()),
}

for direct in DIRECTORIES.values():
    create_dir(direct)
