#!/bin/sh
for file in RCS/*; do
    if rlog "$file" | grep -q "locks:"; then
        echo "$(basename "$file" .v) is locked"
    fi
done
