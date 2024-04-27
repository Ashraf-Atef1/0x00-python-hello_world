#!/usr/bin/python3
import sys
import requests

"""Python script that takes in a URL, sends a request to the URL and displays
the value ofthe X-Request-Idvariable found in the header of the response"""


if __name__ == "__main__":
    with requests.get(sys.argv[1]) as res:
        print(res.headers["X-Request-Id"])
