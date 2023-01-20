#!/usr/bin/python3
<<<<<<< HEAD
"""
Sends a POST request to a given URL with a given email
  - Displays the body of the response.
=======
"""a Python script that takes in a URL and an email,
   sends a POST request to the passed URL
>>>>>>> b6c7c81b3f06f7b93dc40c6b1aeb81568162b2eb
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
