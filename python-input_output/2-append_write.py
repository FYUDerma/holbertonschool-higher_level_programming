#!/usr/bin/python3
"""Defines a text file-reading function."""


def append_write(filename="", text=""):
    """Writes text to a UTF8 text file."""
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
