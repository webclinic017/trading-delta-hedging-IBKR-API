import threading
import time

import pytest
from dotenv import dotenv_values
from loguru import logger
from trading.api.ibapi_class import IBapi

env_vars = dotenv_values(".env")


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

    while True:
        if isinstance(appl.nextorderId, int):
            logger.info('We are connected')
            break
        else:
            print('Waiting for connection... (retrying)')
            time.sleep(1)

    return appl
