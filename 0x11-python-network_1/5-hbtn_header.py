#!/usr/bin/python3
from sys import argv
import requests
"""Python script that takes in a URL, sends a request to the URL and displays 
the value ofthe X-Request-Idvariable found in the header of the response"""


with requests.get(argv[1]) as res:
    print(res.headers['X-Request-Id'])