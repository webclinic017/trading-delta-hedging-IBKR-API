"""Module to define stock contract."""

from ibapi.contract import Contract


def get_apple_contract() -> Contract:
    """apple stock contract."""
    contract = Contract()
    contract.symbol = 'AAPL'
    contract.secType = 'STK'
    contract.exchange = 'SMART'
    contract.currency = 'USD'

    return contract


def get_rklb_contract() -> Contract:
    """rklb stock contract."""
    contract = Contract()
    contract.symbol = 'RKLB'
    contract.secType = 'STK'
    contract.exchange = 'SMART'
    contract.currency = 'USD'

    return contract
