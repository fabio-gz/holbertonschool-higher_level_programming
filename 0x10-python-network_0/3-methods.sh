#!/bin/bash
# displays all HTTP methods
curl -Is "$1" | grep Allow: | cut -d " " -f 2,3,4
