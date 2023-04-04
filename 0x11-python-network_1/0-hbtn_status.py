#!/usr/bin/python3
#Write a Python script that fetches https://alx-intranet.hbtn.io/status
import urllib.request

url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    html = response.read()
if __name__ == "__main__":
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode('utf-8')))

