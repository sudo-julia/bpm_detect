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
        config: ConfigParser = ConfigParser()
        config["DEFAULT"] = {
            "DownloadDirectory": str(DIRECTORIES["DOWNLOAD_BASE_PATH"])
        }
        with configfile.open("w") as file:
            config.write(file)
    raise NotImplementedError("This should return config values or something")


NAME: str = "bpm_detector"

# TODO (jam) config file for these locations
DIRECTORIES: dict[str, Path] = {
    "CONFIG_DIR": Path(appdirs.user_config_dir(NAME)),
    "DOWNLOAD_BASE_PATH": Path(get_downloads_dir()),
}

for direct in DIRECTORIES.values():
    create_dir(direct)

IDS: dict[str, str] = {
    "CLIENT_ID": "",
    "CLIENT_SECRET": "",
    "USER_ID": "",
}
