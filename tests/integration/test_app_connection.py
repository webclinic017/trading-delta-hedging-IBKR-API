import time

from dotenv import dotenv_values
from ibapi.contract import Contract
from trading.api.main import main

env_vars = dotenv_values(".env")


def test_connect_app(aapl_stock_contract: Contract) -> None:

    app = main()
    assert app.isConnected() is True
    assert app.connState == 2

    app.reqMktData(1, aapl_stock_contract, '', False, False, [])
    time.sleep(2.0)  # allow for the connection to be made

    assert isinstance(app.test_apple_stock_price, float)
    assert app.test_market_is_live is True

    app.disconnect()


# def test_data_is_live(aapl_stock_contract: Contract) -> None:
#
#     app = main()
#     # assert app.test_market_is_live is True
#     print("we are here", app.test_apple_stock_price)
#     assert isinstance(app.test_apple_stock_price, float)
#     app.disconnect()
