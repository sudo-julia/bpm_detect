"""get the user's downloads directory, independent of OS"""
# pylint: disable=C0415, E0401
import os


def get_downloads_dir() -> str:
    """get the download path"""
    name: str = os.name
    if name == "nt":
        import winreg

        sub_key: str = (
            r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders"
        )
        downloads_guid = "{374DE290-123F-4565-9164-39C4925E467B}"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    # TODO (jam) see if "Downloads" or "downloads" is in use, check XDG_DOWNLOAD_DIR
    return os.path.join(os.path.expanduser("~"), "downloads")
