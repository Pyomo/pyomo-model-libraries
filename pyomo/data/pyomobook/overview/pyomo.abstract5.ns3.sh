#!/bin/sh

# @cmd:
pyomo --solver=glpk --ns=c1 --ns=data2 abstract5.py \
                        abstract5-ns2.dat
# @:cmd
cat results.yml
