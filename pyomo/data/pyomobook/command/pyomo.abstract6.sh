#!/bin/sh

# @cmd:
pyomo solve -q --model-name=Model abstract6.py abstract6.dat
# @:cmd
cat results.yml
