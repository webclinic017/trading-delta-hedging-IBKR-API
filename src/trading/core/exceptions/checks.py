"""Implement checks and raise errors"""

from trading.api.ibapi_class import IBapi
from trading.core.exceptions.exceptions import PriceNotFloatError, PriceNotLiveError


def check_price_is_live_and_is_float(app: IBapi, stock_request_id: None | int) -> None:
    """Perform some checks for a request on a given stock."""
    ticker_symbol = app.dic_orderid_to_ticker[stock_request_id]

    if not app.stock_price_dic[ticker_symbol].market_is_live:
        raise PriceNotLiveError("Terminating process due to price not being live.")

    if not isinstance(app.stock_price_dic[ticker_symbol].price, float):
        raise PriceNotFloatError(f"Terminating process due to price not being of float type: "
                                 f"got type {type(app.stock_price_dic[ticker_symbol].price)}")

    else:
        if app.stock_price_dic[ticker_symbol].price < 0:  # type: ignore
            raise PriceNotFloatError(f"Terminating process due to price being negative: "
                                     f"got price {app.stock_price_dic[ticker_symbol].price}")
