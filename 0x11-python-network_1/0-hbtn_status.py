#!/usr/bin/python3
# Fetches https://alx-intranet.hbtn.io/status
import urllib.request as browser

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    req = browser.Request(url)

    with browser.urlopen(req) as response:
        body = response.read()

        print("Body response:")
        print('\t- type: {}'.format(type(body)))
        print('\t- content: {}'.format(body))
        print('\t- utf8 content: {}'.format(body.decode("utf-8")))
