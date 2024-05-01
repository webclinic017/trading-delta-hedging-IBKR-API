"""Define custom exceptions"""


class PriceNotLiveError(Exception):
    """custom exception for when the price is not live."""

    pass


class PriceNotFloatError(Exception):
    """custom exception for when the price is not a float type."""

    pass


class NextValidOrderError(Exception):
    """custom exception for when the price is not a float type."""

    pass
