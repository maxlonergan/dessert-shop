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
    '''
    payment class
    '''
    def __init__(self, pay_type=PayType(1).name):
        self._pay_type = pay_type

    @property
    # @abstractmethod
    def pay_type(self):
        return self._pay_type

    @pay_type.setter
    def pay_type(self, new_type):
        # self._pay_type = new_type
        if new_type == 1 or 2 or 3:
            self._pay_type = PayType(new_type).name
        else:
            print('it dont work')
