"""Ibapi Class that inherits from both EWrapper and EClient."""

from ibapi.client import EClient
from ibapi.common import TickAttrib
from ibapi.wrapper import EWrapper
from loguru import logger


class IBapi(EWrapper, EClient):
    """Ibapi Class that inherits from both EWrapper and EClient. This is where the logic for handling incoming messages
    through the Ewrapper happens.
    """

    def __init__(self) -> None:
        """Define variables to be assigned returned value from the Ewrapper"""
        EClient.__init__(self, self)
        self.test_apple_stock_price: float | None = None
        self.test_market_is_live: bool = False

    def tickPrice(self, reqId: int, tickType: int, price: float, attrib: TickAttrib) -> None:
        """Ewrapper method to receive price information from reqMktData()."""
        if tickType == 2 and reqId == 1:
            self.test_apple_stock_price = price
            logger.info(f'The current ask price is: {price}')

    def marketDataType(self, reqId: int, marketDataType: int) -> None:
        """Ewrapper method to receive if market data is live/delayed/frozen from reqMktData()."""
        if reqId == 1 and marketDataType == 1:
            self.test_market_is_live = True
            logger.info(f'Live data is: {self.test_market_is_live}')
