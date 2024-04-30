import threading

import pytest
from dotenv import dotenv_values
from ibapi.contract import Contract
from trading.api.contracts.stock_contracts import get_stock_contract
from trading.api.ibapi_class import IBapi

env_vars = dotenv_values(".env")


@pytest.fixture()
def aapl_stock_contract() -> Contract:

    contract = get_stock_contract("TSLA")

    return contract


@pytest.fixture()
def app() -> IBapi:
    def run_loop() -> None:
        appl.run()

    appl = IBapi()
    appl.connect(env_vars.get("IP_ADDRESS"),
                 int(env_vars.get("PORT")),
                 int(env_vars.get("CLIENT_ID")))

    api_thread = threading.Thread(target=run_loop, daemon=True)
    api_thread.start()

    return appl
