#!/usr/bin/python3
#Python script that takes 2 arguments in order to solve this challenge where the Holberton School staff evaluates candidates applying for a back-end position with multiple technical challenges
import requests
import sys

# Get repository name and owner name from command line arguments
repo_name = sys.argv[1]
owner_name = sys.argv[2]

# Construct the API endpoint URL
url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

# Send GET request to the GitHub API
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    # Parse the response as JSON
    commits = response.json()
    # Print the 10 most recent commits
    for commit in commits[:10]:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
else:
    print(f"Error: {response.status_code} - Failed to fetch commits")

