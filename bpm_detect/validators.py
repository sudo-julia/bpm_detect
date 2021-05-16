#!/usr/bin/env python3
"""validate a spotify uri"""

import regex
from prompt_toolkit.validation import ValidationError, Validator


# pylint: disable=R0903
class PlaylistURIValidator(Validator):
    """validate a playlist uri"""

    def validate(self, document):
        if document.text == "back":
            return "back"
        match = regex.match("^(spotify:playlist:)([a-zA-Z0-9]+)(.*)$", document.text)
        if not match:
            msg = """
            Please provide a valid playlist uri (example: 'spotify:playlist:<id>')"""
            raise ValidationError(
                message=msg,
                cursor_position=len(document.text),  # move cursor to end
            )


# TODO (jam) integrate this in the validator
def convert_url_to_uri(url):
    """convert a url to a uri"""
    match = regex.match(
        r"^https?:\/\/(www\.)?open\.spotify\.com\/playlist\/[a-zA-Z0-9]{23}$",
        url
    )
    if not match:
        return False
    return f"spotify:playlist:{url[-22:]}"
