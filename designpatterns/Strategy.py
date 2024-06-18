from abc import ABC, abstractmethod

class FilterStrategy(ABC):

    @abstractmethod
    def removeValue(self, val):
        pass

class RemoveNegativeStrategy(FilterStrategy):
    def removeValue(self, val):
        super().removeValue(val)
        return val < 0
    
class RemoveOddStrategy(FilterStrategy):
    def removeValue(self, val):
        super().removeValue(val)
        return abs(val) % 2
    
class Values:
    def __init__(self, vals) -> None:
        self.vals = vals

    def filter(self, strategy):
        res = []
        for n in self.vals:
            if not strategy.removeValue(n):
                res.append(n)
        return res
    
values = Values([-7,-4,-1,0,2,6,9])

values.filter(RemoveNegativeStrategy())
values.filter(RemoveOddStrategy())

'''
Defines a family of algorithms, encapsulates each one, and makes them interchangeable. 
Strategy lets the algorithm vary independently from clients that use it.
'''

class Strategy:
    def execute(self, data):
        pass

class ConcreteStrategyA(Strategy):
    def execute(self, data):
        return sorted(data)

class ConcreteStrategyB(Strategy):
    def execute(self, data):
        return sorted(data, reverse=True)

class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def execute_strategy(self, data):
        return self.strategy.execute(data)

# Usage
data = [3, 1, 2]
context = Context(ConcreteStrategyA())
print(context.execute_strategy(data))  # [1, 2, 3]

context.set_strategy(ConcreteStrategyB())
print(context.execute_strategy(data))  # [3, 2, 1]
