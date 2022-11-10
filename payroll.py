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
    def __init__(self, hourly_rate) -> None:
        super().__init__()
        self.hourly_rate = hourly_rate
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
    '''
    manage employee attributes
    change employee's classification
    initiate payment to employee
    '''
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

with open('employees.csv', 'r') as emp:
    lines = [line.strip() for line in emp]
employee_list = [line.split(',') for line in lines]

def load_employees(emp_list):
    '''
    takes the list created from the csv file and should
    return a list of employee objects
    '''
    final_list = []
    for employee in emp_list:
        ident = employee[0]
        fname = employee[1]
        lname = employee[2]
        addy = employee[3]
        city = employee[4]
        state = employee[5]
        zipcode = employee[6]
        classification = employee[7]
        worker = Employee(ident, fname, lname, addy, city, state, zipcode, classification)
        final_list.append(worker)
    final_list.remove(final_list[0])
    return final_list

def find_employee_by_id(ident, all_employees):
    '''
    finds and returns an employee object based on the id number
    test with 51-4678119
    '''
    for employee in all_employees:
        if str(ident) == employee.emp_id:
            return employee

worker_list = load_employees(employee_list)
test_employee = worker_list[0]

print(find_employee_by_id('51-4678119', worker_list).first_name)
