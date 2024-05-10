"""Place (submit) various order types to the TWS API"""

from trading.api.contracts.stock_contracts import get_stock_contract
from trading.api.ibapi_class import IBapi
from trading.api.orders.stock_orders import create_parent_order, create_profit_taker_child_order


def place_simple_order(app: IBapi, ticker_symbol: str, action: str, price: float, quantity: int) -> None:
    """Place a limit order.
    action: str (SELL OR BUY)
    price: float (price for the limit order)
    quantity: int (number of shares)
    """
    contract = get_stock_contract(ticker_symbol)
    order = create_parent_order(app.nextorderId, action, price, quantity)  # type: ignore
    order.transmit = True
    app.placeOrder(app.nextorderId, contract, order)
    app.reqIds(-1)  # increment the next valid id (appl.nextorderId)


def place_profit_taker_order(app: IBapi, ticker_symbol: str, price: float, quantity: int) -> None:
    """Place a limit order.
    action: str (SELL OR BUY)
    price: float (price for the limit order)
    quantity: int (number of shares)
    """
    contract = get_stock_contract(ticker_symbol)
    parent_order = create_parent_order(app.nextorderId, "BUY", price, quantity)  # type: ignore
    parent_order.transmit = False
    profit_taker_child_order = create_profit_taker_child_order(app.nextorderId, app.nextorderId+1, price, quantity)  # type: ignore
    profit_taker_child_order.transmit = True
    app.placeOrder(parent_order.orderId, contract, parent_order)
    app.placeOrder(profit_taker_child_order.orderId, contract, profit_taker_child_order)
    app.reqIds(-1)  # increment the next valid id (appl.nextorderId)
