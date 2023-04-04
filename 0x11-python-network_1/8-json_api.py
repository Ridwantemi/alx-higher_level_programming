#!/usr/bin/python3
#Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
import requests
import sys

# Get the letter from command line argument or set it to empty string if not provided
q = sys.argv[1] if len(sys.argv) > 1 else ""

# Make a POST request to the specified URL with the letter as a parameter
response = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})

# Check if the response has a valid JSON body
if response.ok and response.headers.get('content-type') == 'application/json':
    try:
        data = response.json()
        # Check if the JSON is not empty
        if data:
            # Display id and name for each item in the response
            for item in data:
                print("[{}] {}".format(item.get("id"), item.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
else:
    # Display error code if HTTP status code is >= 400
    print("Error code: {}".format(response.status_code))

