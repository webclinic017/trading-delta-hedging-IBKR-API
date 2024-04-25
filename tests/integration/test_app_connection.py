import time

from ibapi.contract import Contract
from trading.api.main import main


def test_connect_app() -> None:

    app = main()
    assert app.isConnected() is True
    assert app.connState == 2
    app.disconnect()


def test_data_is_live(aapl_stock_contract: Contract) -> None:
    app = main()
    app.reqMktData(1, aapl_stock_contract, '', False, False, [])
    time.sleep(10)
    assert app.market_is_live is True
    app.disconnect()
