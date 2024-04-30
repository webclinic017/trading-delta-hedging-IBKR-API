"""Ibapi Class that inherits from both EWrapper and EClient."""

from dotenv import dotenv_values
from ibapi.client import EClient
from ibapi.common import TickAttrib
from ibapi.wrapper import EWrapper
from loguru import logger

from trading.core.data_models.data_models import StockInfo
from trading.utils import config_load

env_vars = dotenv_values(".env")
config_vars = config_load("./config.yaml")


class IBapi(EWrapper, EClient):
    """Ibapi Class that inherits from both EWrapper and EClient. This is where the logic for handling incoming messages
    through the Ewrapper happens.
    """

    def __init__(self) -> None:
        """Define variables to be assigned returned value from the Ewrapper"""
        EClient.__init__(self, self)

        # build a dic for each stock
        self.stock_price_dic = {}
        for stock_dic in config_vars["stocks"]:
            self.stock_price_dic[stock_dic["reqid"]] = StockInfo(stock=stock_dic["ticker"], reqid=stock_dic["reqid"])

    def tickPrice(self, reqId: int, tickType: int, price: float, attrib: TickAttrib) -> None:
        """Ewrapper method to receive price information from reqMktData()."""
        if tickType == 2:
            self.stock_price_dic[reqId].price = price
            logger.info(f'The current ask price is: {price} for stock {self.stock_price_dic[reqId].stock}.')

    def marketDataType(self, reqId: int, marketDataType: int) -> None:
        """Ewrapper method to receive if market data is live/delayed/frozen from reqMktData()."""
        if marketDataType == 1:
            self.stock_price_dic[reqId].market_is_live = True
            logger.info(
                f'Live data is: {True} for stock {self.stock_price_dic[reqId].stock}.')
