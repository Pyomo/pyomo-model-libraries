#!/bin/sh

pyomo solve --solver=glpk MiscAbstract.py MiscAbstract.dat
cat results.yml
