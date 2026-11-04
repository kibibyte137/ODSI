#!/bin/sh
printf 'Content-Type: text/plain; charset=utf-8\n\n'
echo "Efektywny UID: $(id -u)"
echo "Efektywny GID: $(id -g)"
echo "REMOTE_USER: ${REMOTE_USER:--}"
echo
for f in /lab-data/ogolny.txt /lab-data/poufny.txt; do
    if tresc=$(cat "$f" 2>/dev/null); then
        echo "$f: $tresc"
    else
        echo "$f: odmowa odczytu (brak uprawnien)"
    fi
done