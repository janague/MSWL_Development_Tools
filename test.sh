#!/bin/bash

./webspider.py  -n 1 http://herraiz.org | tail -n 10
./webspider.py  -n 2 http://herraiz.org | tail -n 10
./webspider.py  -n 3 http://herraiz.org | tail -n 10
