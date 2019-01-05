#!/bin/bash
tickers=( XBTUSD ETHXBT )

# ps -e | grep python
# pkill -9 python 
# killall python
python main.py XBTUSD & python main.py ETHXBT