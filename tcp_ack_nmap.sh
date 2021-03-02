#!/bin/bash
nmap -v -sA cora-vuetify-dev.herokuapp.com >>TCPACKScan.txt && cat TCPACKScan.txt
