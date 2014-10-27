#!/bin/sh

# @cmd:
pyomo solve --solver=glpk --solver-options='mipgap=1' concrete1.py
# @:cmd
cat results.yml
