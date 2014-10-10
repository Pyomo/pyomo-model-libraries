#!/bin/sh

pyomo --solver=glpk MiscAbstract2.py MiscAbstract.dat -c
cat results.yml
