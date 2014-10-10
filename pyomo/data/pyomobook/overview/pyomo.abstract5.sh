#!/bin/sh

# @cmd:
pyomo --solver=glpk abstract5.py abstract5.dat
# @:cmd
cat results.yml
