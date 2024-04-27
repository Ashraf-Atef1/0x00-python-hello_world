#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and displays
the value ofthe X-Request-Idvariable found in the header of the response"""
from sys import argv
import requests


if __name__ == "__main__":
    with requests.get(argv[1]) as res:
        print(res.headers.get("X-Request-Id"))
