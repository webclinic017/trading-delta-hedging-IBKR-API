"""Define custom exceptions"""

from trading.api.ibapi_class import IBapi


class PriceNotLiveError(Exception):
    """custom exception for when the price is not live."""

    pass


class PriceNotFloatError(Exception):
    """custom exception for when the price is not a float type."""

    pass


def check_price_is_live_and_is_float(app: IBapi, stock_request_id: int) -> None:
    """Perform some checks for a request on a given stock."""
    if not app.stock_price_dic[stock_request_id].market_is_live:
        raise PriceNotLiveError("Terminating process due to price not being live.")

    if not isinstance(app.stock_price_dic[stock_request_id].price, float):
        raise PriceNotFloatError(f"Terminating process due to price not being of float type: "
                                 f"got type {type(app.stock_price_dic[stock_request_id].price)}")

    else:
        if app.stock_price_dic[stock_request_id].price < 0:  # type: ignore
            raise PriceNotFloatError(f"Terminating process due to price being negative: "
                                     f"got price {app.stock_price_dic[stock_request_id].price}")
