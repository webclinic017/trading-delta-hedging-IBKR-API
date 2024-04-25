"""Ibapi Class that inherits from both EWrapper and EClient."""

from ibapi.client import EClient
from ibapi.common import TickAttrib
from ibapi.wrapper import EWrapper


class IBapi(EWrapper, EClient):
    """Ibapi Class that inherits from both EWrapper and EClient. This is where the logic for handling incoming messages
    through the Ewrapper happens.
    """

    def __init__(self) -> None:
        """Define variables to be assigned returned value from the Ewrapper"""
        EClient.__init__(self, self)
        self.apple_stock_price: float | None = None
        self.market_is_live: bool | None = None

    def tickPrice(self, reqId: int, tickType: int, price: float, attrib: TickAttrib) -> None:
        """Ewrapper method to receive price information from reqMktData()."""
        if tickType == 2 and reqId == 1:
            self.apple_stock_price = price
            print('The current ask price is: ', price)

    def marketDataType(self, reqId: int, marketDataType: int) -> None:
        """Ewrapper method to receive if market data is live/delayed/frozen from reqMktData()."""
        if reqId == 1:
            print("MarketDataType. ReqId:", reqId, "Type: 1=live, 2=frozen, 3=delayed", marketDataType)
            if marketDataType == 1:
                self.market_is_live = True
            else:
                self.market_is_live = False

        print("INSIDE THE FUNC 2", self.market_is_live)
