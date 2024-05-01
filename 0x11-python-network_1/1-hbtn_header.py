#!/usr/bin/python3
# Fetches https://alx-intranet.hbtn.io/status
import urllib.request as browser
import sys

url = sys.argv[1]
req = browser.Request(url)

with browser.urlopen(req) as response:
    body = dict(response.headers)

    print(body.get("X-Request-Id"))
