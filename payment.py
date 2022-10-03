'''
Containts the Payment Class
'''
from abc import ABC
from enum import Enum

class PayType(Enum):
    CASH = 1
    CARD = 2
    PHONE = 3

class Payment(ABC):
    @property
    def pay_type(self):
        self.pay_type = PayType.CASH
