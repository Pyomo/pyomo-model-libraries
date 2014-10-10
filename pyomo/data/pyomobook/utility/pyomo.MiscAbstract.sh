#!/bin/sh

pyomo --solver=glpk MiscAbstract.py MiscAbstract.dat
cat results.yml
