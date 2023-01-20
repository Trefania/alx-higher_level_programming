#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL
"""
if __name__ == "__main__":
    import urllib.request as request
    from sys import argv

    req = request.Request(argv[1])
    with request.urlopen(req) as r:
        print(r.headers.get('X-Request-Id'))
