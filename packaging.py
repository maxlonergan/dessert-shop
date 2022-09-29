from abc import ABC, abstractmethod


class Packaging(ABC):
    def __init__(self, package_type):
        self.package_type = package_type

    @property
    def get_packaging(self):
        return self.package_type

    @property
    @abstractmethod 
    def set_packaging(self, package):
        self.package_type = package
    
    @classmethod
    def __subclasshook__(cls, C):
        if cls is Packaging:
            if any('Get_packaging' in Candy.__dict__ for Candy in C.__mro__):
                pass
            return True
        else:
            return False
        