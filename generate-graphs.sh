#/bin/bash

for file in ./docs/graphs/*
do
    if [[ -f $file ]]; then
        filename=$(basename -- "$file")
        filename="${filename%.*}"
        mmdc -i $file -o ./docs/images/$filename.png -b transparent
    fi
done
