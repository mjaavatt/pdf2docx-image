#!/usr/bin/env bash

if [[ $# -eq 0 ]] ; then
    echo 'Usage'
    echo "$0 input.pdf"
    exit 1
fi

tmp_dir=$(mktemp -d -t ci-XXXXXXXXXX)
filename=$RANDOM

convert -density 300 -background white -alpha remove -bordercolor black -border 5 "$1" "$tmp_dir/$filename-%03d.png"
python "$(dirname "${BASH_SOURCE[0]}")/pdf2docx-image.py" "$tmp_dir/$filename"
outputfilename=$(basename -- "$1")
mv demo.docx "${outputfilename%.*}.docx"
rm -rf "$tmp_dir"
