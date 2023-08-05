#!/usr/bin/env python3

import os
import sys
print(sys.path)

def print_python_env():
    envs = ['PYTHONPATH', 'PYTHONHOME']
    for name in envs:
        print(f"{name} ==> {os.getenv(name)}")

print_python_env()

import whereisdis

