import pytest
from ibapi.contract import Contract


@pytest.fixture()
def aapl_stock_contract() -> Contract:

    apple_contract = Contract()
    apple_contract.symbol = 'AAPL'
    apple_contract.secType = 'STK'
    apple_contract.exchange = 'SMART'
    apple_contract.currency = 'USD'

    return apple_contract
