#!/bin/sh

## (i)nspect data files

(head -n 5; tail -n 5) < "$1" | column -t;
