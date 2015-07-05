#!/bin/sh

echo 'log: "'
pyomo solve --solver=glpk MiscAbstract.py MiscAbstract.dat
echo '"'
cat results.yml
