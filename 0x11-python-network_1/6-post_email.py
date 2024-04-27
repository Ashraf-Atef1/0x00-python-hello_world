#!/usr/bin/python3
import sys
import requests

"""Python script that takes in a URL, sends a request to the URL and displays
the value ofthe X-Request-Idvariable found in the header of the response"""


if __name__ == "__main__":
    url = sys.argv[1]
    values = {"email": sys.argv[2]}
    with requests.post(sys.argv[1], data=values) as res:
        print(res.text)
