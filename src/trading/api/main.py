"""main module that implements the trading app and connects to IBKR API."""


import multiprocessing

# import threading
import time

from dotenv import dotenv_values

from trading.api.ibapi_class import IBapi
from trading.api.stock_contracts import get_apple_contract
from trading.core.exceptions.exceptions import PriceNotLiveError

env_vars = dotenv_values(".env")


def main() -> IBapi:
    """connect to IBapi TWS client"""
    def run_loop() -> None:
        appl.run()

    appl = IBapi()
    appl.connect(env_vars.get("IP_ADDRESS"),
                 int(env_vars.get("PORT")),
                 int(env_vars.get("CLIENT_ID")))

    api_proc = multiprocessing.Process(target=run_loop, args=())
    api_proc.start()

    # api_thread = threading.Thread(target=run_loop, daemon=True)
    # api_thread.start()

    aapl_stock_contract = get_apple_contract()
    appl.reqMktData(1, aapl_stock_contract, '', False, False, [])

    time.sleep(2)

    if not appl.test_market_is_live:
        api_proc.terminate()
        raise PriceNotLiveError("Terminating thread due to price not being live.")

    return appl


if __name__ == '__main__':
    app = main()
