#!/usr/bin/python3
#Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header
import requests
import sys

# Check if the URL is provided as an argument
if len(sys.argv) < 2:
    print("Error: URL not provided")
    sys.exit(1)

# Get the URL from the command line argument
url = sys.argv[1]

# Send GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Check if 'X-Request-Id' header is present in the response
    if 'X-Request-Id' in response.headers:
        # Display the value of 'X-Request-Id' header
        print("{}".format(response.headers['X-Request-Id']))
    else:
        print("Error: 'X-Request-Id' header not found in response")
else:
    print("Error: Request failed with status code {}".format(response.status_code))

