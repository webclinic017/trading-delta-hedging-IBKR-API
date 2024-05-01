"""Module to define stock contract."""

from ibapi.contract import Contract


def get_stock_contract(ticker: str) -> Contract:
    """apple stock contract."""
    contract = Contract()
    contract.symbol = ticker
    contract.secType = 'STK'
    contract.exchange = 'SMART'
    contract.currency = 'USD'

    return contract
