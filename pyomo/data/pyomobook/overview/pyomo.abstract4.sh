#!/bin/sh

pyomo --solver=glpk abstract4.py
cat results.yml
