import time

from dotenv import dotenv_values
from ibapi.contract import Contract
from trading.api.ibapi_class import IBapi

env_vars = dotenv_values(".env")


def app_connection(appl: IBapi) -> None:
    assert appl.isConnected() is True
    assert appl.connState == 2


def data_is_live(appl: IBapi, aapl_contract: Contract) -> None:

    apple_req_id = int(env_vars["TSLA"])
    appl.reqMktData(apple_req_id, aapl_contract, '', False, False, [])
    time.sleep(5)  # allow for the connection to be made
    assert appl.stock_price_dic[apple_req_id].market_is_live is True
    assert isinstance(appl.stock_price_dic[apple_req_id].price, float)


def test_full_app(app: IBapi, aapl_stock_contract: Contract) -> None:

    app_connection(app)
    data_is_live(app, aapl_stock_contract)
    app.disconnect()
