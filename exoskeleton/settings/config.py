"""Utilities for settings handling, reading etc."""
import sys
import yaml


def read_settings(path):
    """Read settings file, return it's contents as dictionary."""

    with open(path, "r") as settingsfile:
        return yaml.load(settingsfile, Loader=yaml.BaseLoader)


def dump_settings(settings_object):
    """Display parsed settings in human readable form."""
    yaml.dump(settings_object, sys.stdout)
