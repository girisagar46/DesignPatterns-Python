from StrategyPattern.strategy_variation import Order, ShippingCost


def fedex_strategy(order):
    return 3.00

ups_strategy = lambda order: 4.00

order = Order()

# fedex
strategy = fedex_strategy
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
print(cost == 3.00)


# ups
strategy = ups_strategy
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
print(cost == 4.00)


# postal
cost_calculator = ShippingCost(lambda order: 5.00)
cost = cost_calculator.shipping_cost(order)
print(cost == 5.00)