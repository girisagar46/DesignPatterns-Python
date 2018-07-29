from StrategyPattern.strategy.stragegy_abc import AbsStrategy


class UpsStrategy(AbsStrategy):

    def calculate(self, order):
        return 4.00
