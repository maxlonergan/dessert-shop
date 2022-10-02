'''
Containts the Payment Class
'''
from abc import ABC
from enum import Enum


class Payment(ABC, Enum):
    @property
    def pay_type(self):
        Paytype = Enum


