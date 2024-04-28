import time

from dotenv import dotenv_values
from ibapi.contract import Contract
from trading.api.ibapi_class import IBapi

env_vars = dotenv_values(".env")


def app_connection(appl: IBapi) -> None:
    assert appl.isConnected() is True
    assert appl.connState == 2


def data_is_live(appl: IBapi, aapl_contract: Contract) -> None:

    appl.reqMktData(1, aapl_contract, '', False, False, [])
    time.sleep(2)  # allow for the connection to be made
    assert appl.test_market_is_live is True
    assert isinstance(appl.test_apple_stock_price, float)


def test_full_app(app: IBapi, aapl_stock_contract: Contract) -> None:

    app_connection(app)
    data_is_live(app, aapl_stock_contract)
    app.disconnect()
