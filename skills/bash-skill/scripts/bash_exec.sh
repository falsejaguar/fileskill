#!/bin/bash

COMMAND="$1"
SAFE="$2"

if [ "$SAFE" = "true" ]; then
    if [[ "$COMMAND" =~ rm|chmod|chown|dd|mkfs ]]; then
        echo "safe_mode prevents dangerous commands"
        exit 0
    fi
fi

bash -c "$COMMAND"
