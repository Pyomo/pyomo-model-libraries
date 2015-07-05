#!/bin/sh

echo 'log: "'
pyomo solve --solver=glpk MiscAbstract2.py MiscAbstract.dat -c
echo '"'
cat results.yml
