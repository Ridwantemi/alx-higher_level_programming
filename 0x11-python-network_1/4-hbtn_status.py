#!/usr/bin/python3
#Python script that fetches https://alx-intranet.hbtn.io/status
import requests

# Send GET request to the URL
response = requests.get('https://alx-intranet.hbtn.io/status')

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Display the body of the response with tabulation before each line
    print("Body response:")
    for line in response.text.splitlines():
        print("\t- type: {}".format(type(line)))
        print("\t- content: {}".format(line))
       #print("\t- utf8 content: {}".format(line.decode('utf-8')))
   # else:
        #print("Error: Request failed with status code {}".format(response.status_code))

