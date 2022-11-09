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

class Employee:
    def __init__(self, emp_id, first_name, last_name, address, city, state, zipcode, classification) -> None:
        self.emp_id: str = emp_id
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.address: str = address
        self.city: str = city
        self.state: str = state
        self.zipcode: str = zipcode
        if classification == '3':
            self.classification = Hourly()
        elif classification == '2':
            self.classification = Commissioned()
        elif classification == '1':
            self.classification = Salaried()

test_hourly_employee = Employee('51-4678119', 'Issie', 'Scholard', '11 Texas Court', 'Columbia', 'Missouri','65218', '3')

