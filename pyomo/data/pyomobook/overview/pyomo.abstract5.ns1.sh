#!/bin/sh

# @cmd:
pyomo --solver=glpk --ns=data1 abstract5.py \
                        abstract5-ns1.dat
# @:cmd
cat results.yml
