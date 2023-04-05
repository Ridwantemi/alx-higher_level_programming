#!/usr/bin/python3
#Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8)
import urllib.request
import urllib.error
import sys
if __name__ == "__main__":)
    # Check if URL argument is provided
    if len(sys.argv) < 2:
        print("Error: URL argument is required.")
        sys.exit(1)

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8')
            print("Response body:")
            print(html)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
    except urllib.error.URLError as e:
        print("Error fetching URL: {}".format(e))

