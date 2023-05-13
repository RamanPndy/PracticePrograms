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