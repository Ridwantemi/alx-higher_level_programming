#!/usr/bin/python3
# a Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response
import urllib.request
import sys
 if __name__ == "__main__":

    # Check if URL argument is provided
    if len(sys.argv) < 2:
        print("Error: URL argument is required.")
        sys.exit(1)

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            x_request_id = response.getheader('X-Request-Id')
            if x_request_id:
            print("{}".format(x_request_id))
            else:
            print("X-Request-Id not found in the response header.")
    except urllib.error.URLError as e:
        print("Error fetching URL: {}".format(e))

