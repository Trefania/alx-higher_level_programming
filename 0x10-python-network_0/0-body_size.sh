#!/bin/bash
# sends a request to that URL, and displays the size of the body of the response
curl -sX "$1" | wc -c