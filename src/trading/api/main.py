"""main module that implements the trading app and connects to IBKR API."""

import threading
import time

from dotenv import dotenv_values
from loguru import logger

from trading.api.contracts.stock_contracts import get_stock_contract
from trading.api.ibapi_class import IBapi
from trading.core.exceptions.exceptions import check_price_is_live_and_is_float
from trading.utils import config_load

env_vars = dotenv_values(".env")
config_vars = config_load("./config.yaml")


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

    rklb_stock_contract = get_stock_contract("RKLB")
    rklb_reqid = int(env_vars.get("RKLB"))
    appl.reqMktData(rklb_reqid, rklb_stock_contract, '', False, False, [])

    nvda_stock_contract = get_stock_contract("NVDA")
    nvda_reqid = int(env_vars.get("NVDA"))
    appl.reqMktData(nvda_reqid, nvda_stock_contract, '', False, False, [])

    time.sleep(5)

    check_price_is_live_and_is_float(appl, rklb_reqid)  # check that conditions are met for rklb stock
    check_price_is_live_and_is_float(appl, nvda_reqid)  # check that conditions are met for nvda stock

    logger.info(f"WE ARE HERE {appl.stock_price_dic[rklb_reqid].price}")
    logger.info(f"WE ARE HERE {appl.stock_price_dic[nvda_reqid].price}")

    return appl


if __name__ == '__main__':
    app = main()
