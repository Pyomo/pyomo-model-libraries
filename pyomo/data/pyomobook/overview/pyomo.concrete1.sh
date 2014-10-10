#!/bin/sh

# @cmd:
pyomo --solver=glpk concrete1.py
# @:cmd
cat results.yml
