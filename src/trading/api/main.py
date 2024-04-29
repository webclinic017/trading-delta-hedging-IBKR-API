"""main module that implements the trading app and connects to IBKR API."""

import threading

from dotenv import dotenv_values

from trading.api.ibapi_class import IBapi

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

    # rklb_stock_contract = get_rklb_contract()
    # appl.reqMktData(2, rklb_stock_contract, '', False, False, [])
    #
    # time.sleep(5)
    #
    # if not appl.test_market_is_live:
    #     raise PriceNotLiveError("Terminating process due to price not being live.")

    return appl


if __name__ == '__main__':
    app = main()
