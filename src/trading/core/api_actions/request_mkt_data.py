"""implement request live market data method"""

import time

from trading.api.contracts.stock_contracts import get_stock_contract
from trading.api.ibapi_class import IBapi
from trading.core.exceptions.checks import check_price_is_live_and_is_float


def request_market_data(app: IBapi, ticker_symbol: str) -> None:
    """Request live streaming market data."""
    contract = get_stock_contract(ticker_symbol)
    app.dic_orderid_to_ticker[app.nextorderId] = ticker_symbol
    app.reqMktData(app.nextorderId, contract, '', False, False, [])
    time.sleep(2)
    check_price_is_live_and_is_float(app, app.nextorderId)
    app.reqIds(-1)  # increment the next valid id (appl.nextorderId)
