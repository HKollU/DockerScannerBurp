#!/bin/bash
nmap -v -sS cora-vuetify-dev.herokuapp.com>TCPSYNScan.txt && cat TCPSYNScan.txt
