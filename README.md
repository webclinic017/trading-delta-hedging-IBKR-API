# Project for algorithmic trading of (dynamic) delta hedging


## dev:

* `poetry install`
* `pre-commit install`


## TO DO:

* Look at stocks that have a lot of volume but that do not have frequent small (several cents) short-term price variations.

## Notes:

# Delta Hedging strategy

* If I sell 0DTE, I remove the overnight risk.
* The options (exercising time) expire at 5:30pm ET, on the expiry day (90 mins after market close), after which it cannot be exercised anymore.
* Trade something liquid so that I can still hedge (i.e., buy the shares) after hours, until 5:30pm.
* Trade something that does not have frequent small (several cents) short-term price variations (something like apple or google), compared to the %of premium made
  (basically look at the variation as a % of the premium received).
* Because the fees are calculated depending on the number of shares (and not the total order value), the stock price needs to be expensive.
* Essentially, I want an expensive stock with low volatility (e.g., BKR.B, LMT, NOC, BLK)

I can be looking at around 2% per month -> 0.5% per week.
