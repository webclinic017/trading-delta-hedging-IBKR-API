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

        # next valid order
        self.nextorderId: int | None = None

        self.dic_orderid_to_ticker: dict = {}

        # build a dic for each stock to store price info and market_is_live
        self.stock_price_dic = {}
        for key, values in config_vars["stocks"].items():
            self.stock_price_dic[key] = StockInfo(stock=key)

    def nextValidId(self, orderId: int | None) -> None:
        """Callback function to update the next valid order id"""
        self.nextorderId = orderId
        logger.info(f"The next valid order id is: {self.nextorderId}.")

    def tickPrice(self, reqId: int, tickType: int, price: float, attrib: TickAttrib) -> None:
        """Ewrapper method to receive price information from reqMktData()."""
        if tickType == 2:
            ticker_symbol = self.dic_orderid_to_ticker[reqId]
            self.stock_price_dic[ticker_symbol].price = price
            logger.info(f'The current ask price is: {price} for stock {self.stock_price_dic[ticker_symbol].stock}.')

    def marketDataType(self, reqId: int, marketDataType: int) -> None:
        """Ewrapper method to receive if market data is live/delayed/frozen from reqMktData()."""
        if marketDataType == 1:
            ticker_symbol = self.dic_orderid_to_ticker[reqId]
            self.stock_price_dic[ticker_symbol].market_is_live = True
            logger.info(
                f'Live data is: {True} for stock {self.stock_price_dic[ticker_symbol].stock}.')
