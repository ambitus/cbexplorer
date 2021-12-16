#!/bin/bash

mkdir tests/jzon
mkdir tests/zml
mkdir tests/controlblocks

for yaml in zml-files/*.yaml
do
    ./tests/cbexplorer.sh $yaml tests/controlblocks/
done

touch tests/controlblocks/__init__.py
for plxmap in tests/controlblocks/*.py
do
    echo "from .$(basename $plxmap .py) import $(basename $plxmap .py)" >> tests/controlblocks/__init__.py
done

python3 -m pytest tests/
