"""main module that implements the trading app and connects to IBKR API."""

import threading

from dotenv import dotenv_values

from trading.api.ibapi_class import IBapi
from trading.api.stock_contracts import get_apple_contract

env_vars = dotenv_values(".env")


def main() -> IBapi:
    """connect to IBapi TWS client"""
    def run_loop() -> None:
        appl.run()

    appl = IBapi()
    appl.connect(env_vars.get("IP_ADDRESS"),
                 int(env_vars.get("PORT")),
                 int(env_vars.get("CLIENT_ID")))

    api_thread = threading.Thread(target=run_loop, daemon=True)
    api_thread.start()

    # request live data (code 1)
    # appl.reqMarketDataType(1)

    apple_contract = get_apple_contract()

    # here, we want to use regulatorySnapshot = False (stream of data)
    appl.reqMktData(1, apple_contract, '', False, False, [])

    return appl


if __name__ == '__main__':
    app = main()
