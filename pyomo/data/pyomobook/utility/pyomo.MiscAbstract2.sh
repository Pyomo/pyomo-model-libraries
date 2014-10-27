#!/bin/sh

pyomo solve --solver=glpk MiscAbstract2.py MiscAbstract.dat -c
cat results.yml
