#!/usr/bin/python3
#Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id
import requests
import sys

# Check for correct number of arguments
if len(sys.argv) != 3:
    print("Usage: python github_user_id.py Ridwantemi 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")
    sys.exit(1)

# Get username and personal access token from command line arguments
username = sys.argv[1]
pat = sys.argv[2]

# Construct the URL for the GitHub API
url = f"https://api.github.com/users/{username}"

# Set the headers for the request with Basic Authentication using the personal access token
headers = {
    "Authorization": f"Basic {username}:{pat}",
    "Accept": "application/vnd.github+json"
}

# Send GET request to GitHub API
response = requests.get(url, headers=headers)

# Check if request was successful (status code 200)
if response.status_code == 200:
    # Parse response as JSON
    user = response.json()

    # Extract and display user ID
    print(user["id"])

else:
    # Display error message with status code
    print(f"Error: {response.status_code}")
