#!/bin/sh

pyomo --solver=glpk concrete3.py
cat results.yml
