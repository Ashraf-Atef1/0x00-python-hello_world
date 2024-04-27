#!/usr/bin/python3
from sys import argv
import requests

"""Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)."""


if __name__ == "__main__":
    with requests.get(argv[1]) as res:
        if res.ok:
            print(res.text)
        else:
            print(f"Error code: {res.status_code}")
