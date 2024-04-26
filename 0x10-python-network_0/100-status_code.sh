#!/bin/bash
# Send a GET request and return only the http status code
curl -s -w "%{http_code}" -o /dev/null "$1"
