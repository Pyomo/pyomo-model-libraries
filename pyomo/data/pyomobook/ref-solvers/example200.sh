#!/bin/sh

# @cmd:
pyomo solve --solver=py:cplex simple.py
# @:cmd
cat results.yml
