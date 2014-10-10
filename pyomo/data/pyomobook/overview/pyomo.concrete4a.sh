#!/bin/sh

pyomo --solver=glpk concrete4a.py
cat results.yml
