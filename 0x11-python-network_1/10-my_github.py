#!/usr/bin/python3
"""Uses the GitHub API to display a GitHub ID based on given credentials.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    name = sys.argv[1]
    pssword = sys.argv[2]
    auth = HTTPBasicAuth(name, pssword)
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))