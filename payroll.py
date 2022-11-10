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
    def __init__(self, hourly_rate=10.75) -> None:
        super().__init__()
        self.hourly_rate = hourly_rate

class Salaried(Classification):
    '''
    Know the employee's salary
    Compute the Salaried employee's pay
    '''
    def __init__(self, salary) -> None:
        super().__init__()
        self.salary = salary
    pass

class Commissioned(Salaried):
    '''
    know the employee's commision rate
    add/store new reciepts
    compute commisioned employee's pay (includes salary)
    '''
    def __init__(self, salary, rate) -> None:
        super().__init__(salary)
        self.rate = rate
        self.commission_pay = (salary, rate)
    pass

class Employee:
    '''
    manage employee attributes
    change employee's classification
    initiate payment to employee
    '''
    def __init__(self, emp_id, first_name, last_name, address, city, state, zipcode, classification, pay) -> None:
        self.emp_id: str = emp_id
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.address: str = address
        self.city: str = city
        self.state: str = state
        self.zipcode: str = zipcode
        if classification == '3':
            self.classification = Hourly(pay)
        elif classification == '2':
            salary = pay[0]
            rate = pay[1]
            self.classification = Commissioned(salary, rate)
        elif classification == '1':
            self.classification = Salaried(pay)

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
        if classification == '3':
            hourly_pay = employee[10]
            worker = Employee(ident, fname, lname, addy, city, state, zipcode, classification, hourly_pay)
            final_list.append(worker)
        if classification == '2':
            commission = (employee[8], employee[9])
            worker = Employee(ident, fname, lname, addy, city, state, zipcode, classification, commission)
            final_list.append(worker)
        if classification == '1':
            salary = employee[8]
            worker = Employee(ident, fname, lname, addy, city, state, zipcode, classification, salary)
            final_list.append(worker)

    # final_list.remove(final_list[0])
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
hourly_test = find_employee_by_id('51-4678119', worker_list)
salary_test = find_employee_by_id('11-0469486', worker_list)
commission_test = find_employee_by_id('68-9609244', worker_list)

print(hourly_test.classification.hourly_rate)
print(salary_test.classification.salary)
print(commission_test.classification.commission_pay)


# print(find_employee_by_id('51-4678119', worker_list).first_name)
