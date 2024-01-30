#!/usr/bin/python3
"""Locked class module"""
class LockedClass:
    """ Locked class"""
    def __setattr__(self, name, value):
        if name != "first_name":
            raise AttributeError(
                f"'{self.__class__.__name__}' object has no attribute '{name}'"
            )
