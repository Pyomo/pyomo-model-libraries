#!/bin/sh

# @cmd:
pyomo solve --solver=glpk --ns=data2 abstract5.py \
                        abstract5-ns1.dat
# @:cmd
cat results.yml
