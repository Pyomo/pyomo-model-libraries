#!/bin/sh

pyomo --solver=glpk concrete2.py
cat results.yml
