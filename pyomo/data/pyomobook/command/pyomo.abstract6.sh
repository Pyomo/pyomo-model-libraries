#!/bin/sh

# @cmd:
pyomo solve --solver=glpk --logging=quiet --model-name=Model abstract6.py abstract6.dat
# @:cmd
cat results.yml
