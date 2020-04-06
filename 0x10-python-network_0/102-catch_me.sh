#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me
curl -sX PUT 0.0.0.0:5000/catch_me -L -d "user_id=98" -H "origin:HolbertonSchool"
