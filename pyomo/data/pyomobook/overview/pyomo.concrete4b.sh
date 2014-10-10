#!/bin/sh

pyomo --solver=glpk concrete4b.py
cat results.yml
