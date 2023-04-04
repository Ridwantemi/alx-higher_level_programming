#!/usr/bin/python3
import urllib.parse
import urllib.request
import sys

# Check if URL and email arguments are provided
if len(sys.argv) < 3:
    print("Error: URL and email arguments are required.")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

# Encode email as URL parameter
data = urllib.parse.urlencode({'email': email}).encode('utf-8')

try:
    with urllib.request.urlopen(url, data=data) as response:
        html = response.read().decode('utf-8')
        print("Response body:")
        print(html)
except urllib.error.URLError as e:
    print("Error fetching URL: {}".format(e))

