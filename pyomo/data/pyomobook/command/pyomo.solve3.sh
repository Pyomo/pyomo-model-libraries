#!/bin/sh

# @cmd:
pyomo solve --solver=glpk --solver-suffixes='.*' concrete2.py
# @:cmd
cat results.yml
\rm -f results.csv results.yml
