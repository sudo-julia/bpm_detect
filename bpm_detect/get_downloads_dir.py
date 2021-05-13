"""get the user's downloads directory, independent of OS"""
# pylint: disable=C0415, E0401
from __future__ import annotations
import os
from pathlib import Path


def get_downloads_dir() -> str:
    """get the download path"""
    # get windows downloads path
    name: str = os.name
    if name == "nt":
        import winreg

        sub_key: str = (
            r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders"
        )
        downloads_guid: str = "{374DE290-123F-4565-9164-39C4925E467B}"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            return winreg.QueryValueEx(key, downloads_guid)[0]

    # get unix downloads path
    location: str | None
    if not (location := os.environ.get("XDG_DOWNLOAD_DIR")):
        if Path("~/downloads").expanduser().exists():
            location = str(Path("~/downloads").expanduser())
        else:
            location = str(Path("~/Downloads").expanduser())
    return location
