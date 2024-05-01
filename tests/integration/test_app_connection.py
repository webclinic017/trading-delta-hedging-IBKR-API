import time

from ibapi.contract import Contract
from trading.api.ibapi_class import IBapi
from trading.utils import config_load

config_vars = config_load("./config.yaml")


def app_connection(appl: IBapi) -> None:
    assert isinstance(appl.nextorderId, int)
    assert appl.isConnected() is True
    assert appl.connState == 2


def data_is_live(appl: IBapi, tsla_stock_contract: Contract) -> None:

    apple_req_id = config_vars["stocks"]["TSLA"]["reqid"]
    appl.reqMktData(apple_req_id, tsla_stock_contract, '', False, False, [])
    time.sleep(5)  # allow for the connection to be made
    assert appl.stock_price_dic[apple_req_id].market_is_live is True
    assert isinstance(appl.stock_price_dic[apple_req_id].price, float)


def test_full_app(app: IBapi, tsla_stock_contract: Contract) -> None:

    app_connection(app)
    data_is_live(app, tsla_stock_contract)
    app.disconnect()
