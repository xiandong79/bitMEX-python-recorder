import logging
from time import sleep
import time
import datetime
import pathlib
import sys
from logging.handlers import TimedRotatingFileHandler

from bitmex_websocket import BitMEXWebsocket


def run(symbol, date_string):
    # Basic use of websocket.
    logger = setup_logger(symbol, date_string)

    # Instantiating the WS will make it connect. Be sure to add your api_key/api_secret.
    ws = BitMEXWebsocket(endpoint="https://testnet.bitmex.com/api/v1", symbol=symbol,
                         api_key="zwD49vf_hXhn-jMjC6KSQQIJ", api_secret="1xQwr9p2era1EbRPQJ9qPAviV8nJIvOWx6Sf0vvHqZSHqMot")

    # Run forever
    while(ws.ws.sock.connected):
        logger.info("orderBookL2_25: {}".format(
            ws.market_depth()))
        logger.info("recent_trades: {}".format(ws.recent_trades()))
        sleep(1)


def setup_logger(symbol, date_string):
    # save logger info to files
    logger = logging.getLogger()
    # Change this to DEBUG if you want a lot more info
    logger.setLevel(logging.INFO)
    # add by xiandong
    pathlib.Path('hft_data' + '/' + date_string + '/' +
                 symbol).mkdir(parents=True, exist_ok=True)
    logFilePath = 'hft_data' + '/' + date_string + '/' + symbol + '/log'
    handler = TimedRotatingFileHandler(logFilePath, when="M", interval=1)
    # “M”: Minutes “H”: Hours “D”: Days
    logger.addHandler(handler)
    return logger


if __name__ == "__main__":
    # python main.py ETHXBT
    symbol = str(sys.argv[1])    # symbol="XBTUSD" "ETHXBT"
    date_string = datetime.datetime.now().strftime("%Y%m%d")  # %H:%M:%S"
    run(symbol=symbol, date_string=date_string)
