

from road import Road
from random import randint
from _enum import TrafficConditionEnum

class TrafficCondition:
    def __init__(self, road: Road):
        self.road = road
        self.condition = self._compute_condition(road)
        
    def _get_random_number(self) -> int:
        number = randint(1, 3)
        return number
        
    def _compute_condition(self, road):
        status = self._get_random_number()
        if status == 1:
            return TrafficConditionEnum.LOW
        if status == 2:
            return TrafficConditionEnum.MEDIUM
        if status == 3:
            return TrafficConditionEnum.HIGH
        
    def get_condition(self):
        return self.condition
    
    def set_condition(self, condition):
        self.condition = condition
        