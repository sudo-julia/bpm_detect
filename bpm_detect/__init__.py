"""get the user's config dir"""
import appdirs

# TODO config file, downloads dir
NAME: str = "bpm_detector"

CONFIG_DIR: str = appdirs.user_config_dir(NAME)
DATA_DIR: str = appdirs.user_data_dir(NAME)
# TODO (jam) use appdirs to find default downloads dir, create a subdir for this program
# TODO (jam) config file for this location
DOWNLOAD_BASE_PATH: str = f"{DATA_DIR}/bpm_detect/downloads"
