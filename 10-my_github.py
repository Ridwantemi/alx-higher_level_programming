#!/usr/bin/python3
#Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id
import requests
import sys

if len(sys.argv) < 3:
    print("Usage: python github_commits.py <repository_name> <owner_name>")
    sys.exit(1)

repo_name = sys.argv[1]
owner_name = sys.argv[2]

url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
headers = {
    "Authorization": "Token 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",
    "Accept": "application/vnd.github+json"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    commits = response.json()
    for commit in commits:
        sha = commit["sha"]
        author_name = commit["commit"]["author"]["name"]
        print(f"{sha}: {author_name}")
else:
    print(f"Error: {response.status_code} - {response.json()['message']}")

