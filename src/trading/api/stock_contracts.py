"""Module to define stock contract."""

from ibapi.contract import Contract


def get_apple_contract() -> Contract:
    """apple stock contract."""
    apple_contract = Contract()
    apple_contract.symbol = 'AAPL'
    apple_contract.secType = 'STK'
    apple_contract.exchange = 'SMART'
    apple_contract.currency = 'USD'

    return apple_contract
