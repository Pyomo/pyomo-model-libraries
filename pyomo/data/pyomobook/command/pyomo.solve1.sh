#!/bin/sh

# @cmd:
pyomo --solver=glpk --solver-options='mipgap=1' concrete1.py
# @:cmd
cat results.yml
