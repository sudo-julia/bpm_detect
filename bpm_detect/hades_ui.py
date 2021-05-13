#!/usr/bin/env python3
"""ui for bpm detector"""
import os
from argparse import ArgumentParser

from examples import custom_style_2 as style
from PyInquirer import Separator, prompt

from bpm_detect import DOWNLOAD_BASE_PATH
from bpm_detect.main import Hades
from bpm_detect.validators import PlaylistURIValidator

# Argparser
parser = ArgumentParser(description="Download Spotify playlist the easy way")


class HadesUI:
    def __init__(self, pl_uri=None):
        self.bpm_detect = Hades()

        if pl_uri:
            self.bpm_detect.download_tracks(pl_uri)
        else:
            self.reset_screen()
            self.main_menu()

    def reset_screen(self):
        """clear the screen"""
        os.system("clear")

    def main_menu(self):
        menu = [
            {
                "type": "list",
                "name": "action",
                "message": "Spotify downloader manager",
                "choices": [
                    {"name": "Download from uri", "value": "download_playlist"},
                    {"name": "Manage my playlists", "value": "manage_playlists"},
                    {"name": "Quit", "value": "quit"},
                    Separator(),
                    {
                        "name": "Current download path",
                        "disabled": f"{DOWNLOAD_BASE_PATH}",
                    },
                    {
                        "name": "You can change the download path changing",
                        "disabled": "bpm_detect.py > DOWNLOAD_BASE_PATH",
                    },
                ],
            },
        ]
        answer = prompt(menu, style=style)
        action = getattr(self, answer["action"])
        action()

    def quit(self):
        pass

    def download_playlist(self):
        input = [
            {
                "type": "input",
                "name": "pl_uri",
                "message": "Playlist uri to download:",
                "default": "back",
                "validate": PlaylistURIValidator,
            }
        ]
        response = prompt(input)["pl_uri"]
        if response == "back":
            self.reset_screen()
            self.main_menu()
        else:
            self.bpm_detect.download_tracks(response)

        confirm = [
            {
                "type": "confirm",
                "message": "Download complete. Continue downloading?",
                "name": "continue",
                "default": True,
            }
        ]
        response = prompt(confirm, style=style)["continue"]
        if response:
            self.reset_screen()
            self.main_menu()
        else:
            self.quit()

    def manage_playlists(self):
        playlists = self.bpm_detect.get_user_playlists()
        menu = [
            {
                "type": "checkbox",
                "name": "response",
                "message": "Select playlist to download",
                "choices": playlists,
            }
        ]
        selected_playlists = prompt(menu)["response"]

        for pl in selected_playlists:
            self.bpm_detect.download_tracks(pl)


if __name__ == "__main__":
    parser.add_argument(
        "--pl_uri", metavar="playlist_uri", type=str, help="Spotify playlist uri"
    )
    HadesUI(parser.parse_args().pl_uri)
