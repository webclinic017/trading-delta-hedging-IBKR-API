"""main module that implements the trading app and connects to IBKR API."""

import threading

from dotenv import dotenv_values
from ibapi.client import EClient
from ibapi.wrapper import EWrapper

env_vars = dotenv_values(".env")


class IBapi(EWrapper, EClient):
    """Ibapi Class that inherits from both EWrapper and EClient"""

    def __init__(self) -> None:
        EClient.__init__(self, self)


def connect_app() -> IBapi:
    """connect to IBapi TWS client"""
    def run_loop() -> None:
        appl.run()

    appl = IBapi()
    appl.connect(env_vars.get("IP_ADDRESS"),
                 int(env_vars.get("PORT")),
                 int(env_vars.get("CLIENT_ID")))

    api_thread = threading.Thread(target=run_loop, daemon=True)
    api_thread.start()

    return appl


if __name__ == '__main__':
    app = connect_app()
