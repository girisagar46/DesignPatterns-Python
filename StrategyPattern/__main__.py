from StrategyPattern.strategy import FedExStrategy, PostalStrategy, UpsStrategy
from StrategyPattern.strategy import Order, ShippingCost

order = Order()
strategy = FedExStrategy()  # instantiate Concrete class here
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
print(cost == 3.00)


order = Order()
strategy = PostalStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
print(cost == 5.00)


order = Order()
strategy = UpsStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
print(cost == 4.00)
