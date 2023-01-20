import urllib.error as error
import urllib.request as request
req=request.Request("https://httpbin.org/status/404")

try:
    with request.urlopen(req) as r:
        print(r.read().decode('utf-8'))
except error.HTTPError as e:
    print("Error code: {}".format(e.code))