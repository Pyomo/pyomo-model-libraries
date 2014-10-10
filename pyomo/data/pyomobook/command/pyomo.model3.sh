#!/bin/sh

cd ../overview
# @cmd:
pyomo --instance-only --save-model=concrete1.nl concrete1.py
# @:cmd
diff concrete1.nl ../command/concrete1.nl
