#!/bin/bash
curl -i -s -k -X $'GET' \
    -H $'Host: cora-vuetify-dev.herokuapp.com' -H $'Connection: close' \
    $'https://cora-vuetify-dev.herokuapp.com/robots.txt' >robots.txt && cat robots.txt
