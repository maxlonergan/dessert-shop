'''
Containts the Payment Class
'''
from abc import ABC, abstractmethod
from enum import Enum

class PayType(Enum):
    CASH = 1
    CARD = 2
    PHONE = 3

class Payment(ABC):
    def __init__(self, pay_type):
        self._pay_type = pay_type
    
    @property
    # @abstractmethod
    def pay_type(self):
        return self._pay_type

    @pay_type.setter
    def pay_type(self, new_type):
        if isinstance(new_type, int):
            self._pay_type = new_type
        else:
            print('it dont work')


payment = Payment(5)
payment.pay_type = 3

print(payment.pay_type)