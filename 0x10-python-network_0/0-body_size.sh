#!/bin/bash
# Gets the size in bytes of total response received
echo -e "$(curl -s -w "%{size_download}" -o /dev/null "$1")"
