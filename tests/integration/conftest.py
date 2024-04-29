import pytest
from ibapi.contract import Contract
from trading.api.ibapi_class import IBapi
from trading.api.main import main


@pytest.fixture()
def aapl_stock_contract() -> Contract:

    contract = Contract()
    contract.symbol = 'AAPL'
    contract.secType = 'STK'
    contract.exchange = 'SMART'
    contract.currency = 'USD'

    return contract


@pytest.fixture()
def app() -> IBapi:

    appl = main()

    return appl
