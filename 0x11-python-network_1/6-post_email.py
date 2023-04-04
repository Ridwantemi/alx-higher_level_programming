#!/usr/bin/python3
#Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response
import requests
import sys

# Check if the URL and email address are provided as arguments
if len(sys.argv) < 3:
    print("Error: URL and email address not provided")
    sys.exit(1)

# Get the URL and email address from the command line arguments
url = sys.argv[1]
email = sys.argv[2]

# Define the data to be sent in the POST request
data = {'email': email}

# Send POST request to the URL with the data
response = requests.post(url, data=data)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Display the body of the response
    print("Response body:")
    print(response.text)
else:
    print("Error: Request failed with status code {}".format(response.status_code))

