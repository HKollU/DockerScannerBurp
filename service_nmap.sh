#!/bin/bash
dockscan nmap -v -sV -version-intensity 5 cora-vuetify-dev.herokuapp.com>ServiceScan.txt && cat ServiceScan.txt
