#!/bin/sh

pyomo --solver=glpk concrete2a.py
cat results.yml
