#!/bin/sh

pyomo --solver=glpk concrete5.py
cat results.yml
