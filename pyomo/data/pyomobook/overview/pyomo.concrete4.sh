#!/bin/sh

pyomo --solver=glpk concrete4.py
cat results.yml
