#!/bin/bash
# displays all HTTP methods
curl -s -I "$1" | grep Allow | cut -d ":" -f 2 | xargs
