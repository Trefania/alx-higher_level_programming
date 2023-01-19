#!/usr/bin/python3
"""Python Script that utilises a search API"""

if __name__ == '__main__':
    import sys
    import requests

    url = "http://0.0.0.0:5000/search_user"
    query = "" if len(sys.argv) < 2 else sys.argv[1]
    try:
        dct = {'q': query}
        response = requests.post(url, data=dct)
        result = response.json()
        if result == {}:
            print("No result")
        else:
            print(f"[{result.get('id')}] {result.get('name')}")
    except ValueError:
        print("Not a valid JSON")