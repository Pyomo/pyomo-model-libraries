#!/bin/sh

# @cmd:
pyomo --solver=glpk --postprocess postprocess_fn.py concrete1.py
# @:cmd
cat results.yml
cat results.csv
