#!/bin/sh

# markdown view 
pandoc "$1" | w3m -T text/html

