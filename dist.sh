#!/usr/bin/env sh

rm -rf ./dist
python3 setup.py sdist
twine upload dist/*