#!/bin/bash
# sends a request to that URL, and displays the size of the body of the response
curl -s -I $1 | awk '/^Content-Length/ { print $2 }'
