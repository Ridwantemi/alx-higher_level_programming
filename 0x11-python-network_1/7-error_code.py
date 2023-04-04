#!/usr/bin/python3
Python script that takes in a URL, sends a request to the URL and displays the body of the response
import requests
import sys

# Get the URL from command line argument
url = sys.argv[1]

# Send GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Display the body of the response
    print("Response body:")
    print(response.text)
else:
    # Print error message with status code
    print("Error code: {}".format(response.status_code))

