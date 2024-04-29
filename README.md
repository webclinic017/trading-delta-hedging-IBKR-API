# Project for algorithmic trading of (dynamic) delta hedging


## dev:

* `poetry install`
* `pre-commit install`


## TO DO:

* Search which stock has the least movement between closing price at 4:30pm and opening price at 9:30am (i.e., little movement outside regular trading hours).
* Look at how often the above happens depending on the option's DTE.

## Notes:

* If I sell 0DTE, I remove the overnight risk.
* The options (exercising time) expire at 5:30pm ET, on the expiry day (90 mins after market close), after which it cannot be exercised anymore.
* Trade something very liquid so that I can still hedge (i.e., buy the shares) after hours until 5:30pm.

I can be looking at around 2% per month -> 0.5% per week.
