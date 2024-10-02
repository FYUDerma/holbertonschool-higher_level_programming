#!/usr/bin/python3
"""Defines a text file-reading function."""


def write_file(filename="", text=""):
    """Writes text to a UTF8 text file."""
    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))
