#!/bin/bash

find . -type f ! -name '*.gz' ! -name '*.sh' | while read file; do
    gzip "$file"
done