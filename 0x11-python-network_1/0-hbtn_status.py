#!/usr/bin/python3
import urllib.request
"""Python script that fetches https://alx-intranet.hbtn.io/status"""


with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as res:
    content = res.read()
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
    print("\t- utf8 content:", content.decode('utf-8'))
