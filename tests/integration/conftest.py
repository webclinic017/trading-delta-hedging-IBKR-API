import pytest
from ibapi.contract import Contract
from trading.api.ibapi_class import IBapi
from trading.api.main import main


@pytest.fixture()
def aapl_stock_contract() -> Contract:

    apple_contract = Contract()
    apple_contract.symbol = 'AAPL'
    apple_contract.secType = 'STK'
    apple_contract.exchange = 'SMART'
    apple_contract.currency = 'USD'

    return apple_contract


@pytest.fixture()
def app() -> IBapi:

    appl = main()

    return appl
