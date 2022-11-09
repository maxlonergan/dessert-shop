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

class Salaried(Classification):
    '''
    Know the employee's salary
    Compute the Salaried employee's pay
    '''
    pass

class Commissioned(Salaried):
    '''
    know the employee's commision rate
    add/store new reciepts
    compute commisioned employee's pay (includes salary)
    '''
    pass

