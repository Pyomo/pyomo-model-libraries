#!/bin/sh

# @cmd:
pyomo -q --model-name=Model abstract6.py abstract6.dat
# @:cmd
cat results.yml
