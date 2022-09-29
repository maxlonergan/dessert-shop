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
        pass
        