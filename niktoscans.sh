#!/bin/bash
nikto -Display 1234V -h cora-vuetify-dev.herokuapp.com >niktoScan.txt && cat niktoScan.txt
