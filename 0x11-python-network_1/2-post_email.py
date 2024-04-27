#!/usr/bin/python3
import sys
import urllib.request
import urllib.parse

"""Python script that takes in a URL, sends a request to the URL and displays
the value ofthe X-Request-Idvariable found in the header of the response"""


if __name__ == "__main__":
    url = sys.argv[1]
    values = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode("ascii")
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
