#!/bin/bash

rm .NextMoves/* acro_dicts/* #a bunch of stuff

python3 wikichomp_py3.py
python3 spinylize.py
python3 boardtrim.py
python3 wordsanitizer.py
echo "words sanitized"
python3 nextbestwords.py & 
bestwords=$!
#python3 vertical_land/VERTnextbestwords.py &
vertwords=$!
