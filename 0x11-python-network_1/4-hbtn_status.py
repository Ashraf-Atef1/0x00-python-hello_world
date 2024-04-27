#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    with requests.get("https://alx-intranet.hbtn.io/status") as res:
        r = res.text
        print("Body response:")
        print(f"\t- type: {type(r)}")
        print(f"\t- content: {r}")
