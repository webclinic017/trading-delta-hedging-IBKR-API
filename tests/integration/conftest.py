import pytest
from ibapi.contract import Contract
from trading.api.contracts.stock_contracts import get_stock_contract
from trading.api.ibapi_class import IBapi
from trading.api.main import main


@pytest.fixture()
def aapl_stock_contract() -> Contract:

    contract = get_stock_contract("AAPL")

    return contract


@pytest.fixture()
def app() -> IBapi:

    appl = main()

    return appl
