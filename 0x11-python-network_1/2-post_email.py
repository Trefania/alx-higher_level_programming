#!/usr/bin/python3
""" takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)"""
import urllib.request
import urllib.parse
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    mail = {'email': argv[2]}

    data = urllib.parse.urlencode(mail)
    data = data.encode('ascii')
    # printing the request
    with urllib.request.urlopen(url, data) as response:
        response_page = response.read()
        print(response_page.decode('utf-8'))
