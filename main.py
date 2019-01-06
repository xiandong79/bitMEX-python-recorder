import logging
from time import sleep
import time
import sys

from bitmex_websocket import BitMEXWebsocket


def run(symbol):
    # Basic use of websocket.
    # Instantiating the WS will make it connect. Be sure to add your api_key/api_secret.
    ws = BitMEXWebsocket(endpoint="https://testnet.bitmex.com/api/v1", symbol=symbol,
                         api_key="zwD49vf_hXhn-jMjC6KSQQIJ", api_secret="1xQwr9p2era1EbRPQJ9qPAviV8nJIvOWx6Sf0vvHqZSHqMot")


if __name__ == "__main__":
    # python main.py ETHXBT
    symbol = str(sys.argv[1])    # symbol="XBTUSD" "ETHXBT"
    run(symbol=symbol)
