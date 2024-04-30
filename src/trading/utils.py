"""utility functions used throughout the project."""

import yaml  # type: ignore


def config_load(PATH: str) -> dict:
    """load config file into a dict"""
    with open(PATH) as f:
        return dict(yaml.safe_load(f))
