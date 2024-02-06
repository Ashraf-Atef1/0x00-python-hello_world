#!/usr/bin/python3
"""
This module has a function that
returns the JSON representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """
    This module has a function that
    returns the JSON representation of an object (string)
    """
    try:
        return json.dumps(my_obj)
    except Exception:
        raise TypeError(f"{my_obj} is not JSON serializable")
