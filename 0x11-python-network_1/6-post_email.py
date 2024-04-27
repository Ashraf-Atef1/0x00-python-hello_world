#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and displays
the value ofthe X-Request-Idvariable found in the header of the response"""
from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]
    values = {"email": argv[2]}
    with requests.post(argv[1], data=values) as res:
        print(res.text)
