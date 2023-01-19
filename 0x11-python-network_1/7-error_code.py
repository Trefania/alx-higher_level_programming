#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL
and displays the body of the response"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    r = requests.get(url)
    if hasattr(r, 'status_code') and r.status_code >= 400:
        print(f"Error code: {r.status_code}")
    else:
        print(r.text)
