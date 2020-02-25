#!/usr/bin/sh


# format file name to last modidfication time of FILE 
for f in *; do mv -- $f "$(date -r $f +%Y-%m-%d_%T)"; done

# sort file into month directory
for i in {01..12}; do mv -- 2019-$i-* $i/ ; done


# sort file into date directory
mkdir {01..31}; for i in {01..31}; do mv -- 2019-11-$i* $i/ ; done
