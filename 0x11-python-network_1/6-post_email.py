#!/usr/bin/python3
from sys import argv
import requests
"""Python script that takes in a URL, sends a request to the URL and displays 
the value ofthe X-Request-Idvariable found in the header of the response"""


url = argv[1]
values = {'email' : argv[2]}
with requests.post(argv[1], data=values) as res:
   print(res.text)
