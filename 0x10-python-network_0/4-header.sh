#!/bin/bash
# Send a GET request to a given URL with a Header variable
curl -s -H "X-School-User-Id: 98" "$1"
