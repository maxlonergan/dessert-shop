from abc import ABC

class Classification(ABC):
    '''
    An abstract base class for the three types of classification
    specifies the abstract method issue_payment
    '''
    pass

class Hourly(Classification):
    '''
    know the employees hourly_rate
    add/store new time cards
    compute the Hourly employee's pay
    '''
    pass
