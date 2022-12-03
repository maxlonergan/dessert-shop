from abc import ABC, abstractmethod
import os, os.path, shutil 


class Classification(ABC):
    '''
    An abstract base class for the three types of classification
    specifies the abstract method issue_payment
    '''
    @abstractmethod
    def issue_payment(self):
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
        self.hourly_record = []
        self.total_pay = sum(self.hourly_record)
    def issue_payment(self, emp_name):
        super().issue_payment()
        if not self.hourly_record:
            pay = 0
            return pay
        total_hours = sum(self.hourly_record[0])
        pay = total_hours * float(self.hourly_rate)
        with open('payroll.txt', 'a') as payment_file:
            payment_file.write(f'Mailing ${round(pay, 2)} to {emp_name.full_name} at {emp_name.address}\n')

class Salaried(Classification):
    '''
    Know the employee's salary
    Compute the Salaried employee's pay
    '''
    def __init__(self, salary) -> None:
        super().__init__()
        self.salary = salary
        self.paycheck = float(salary) / 24

    def issue_payment(self, emp_name):
        super().issue_payment()
        paycheck = self.paycheck
        with open('payroll.txt', 'a') as payment_file:
            payment_file.write(f'Mailing ${round(paycheck, 2)} to {emp_name.full_name} at {emp_name.address}\n')

class Commissioned(Salaried):
    '''
    know the employee's commision rate
    add/store new reciepts
    compute commisioned employee's pay (includes salary)
    '''
    def __init__(self, salary, rate) -> None:
        super().__init__(salary)
        self.rate = '.' + str(rate)
        self.paycheck = float(salary) / 24
        self.receipts = []

    def issue_payment(self, emp_name):
        # super().issue_payment()
        if not self.receipts:
            total_pay = self.paycheck
            return total_pay
        reciepts_sum = sum(self.receipts[0])
        commission_pay = float(self.rate) * reciepts_sum
        total_pay = self.paycheck + commission_pay
        with open('payroll.txt', 'a') as payment_file:
            payment_file.write(f'Mailing ${round(total_pay, 2)} to {emp_name.full_name} at {emp_name.address}\n')

    def add_receipt(self, receipt):
        self.receipts[0].append(receipt)

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
        self.full_name: str = f'{first_name} {last_name}'
        self.address: str = f'{address} {city} {state} {zipcode}'
        if classification == '3':
            self.classification = Hourly(pay)
        elif classification == '2':
            salary = pay[0]
            rate = pay[1]
            self.classification = Commissioned(salary, rate)
        elif classification == '1':
            self.classification = Salaried(pay)
    def issue_payment(self):
        '''
        issues payment through each subclasses method issue_payment
        '''
        if isinstance(self.classification, Hourly):
            self.classification.issue_payment(find_employee_by_id(self.emp_id))
        elif isinstance(self.classification, Commissioned):
            self.classification.issue_payment(find_employee_by_id(self.emp_id))
        elif isinstance(self.classification, Salaried):
            self.classification.issue_payment(find_employee_by_id(self.emp_id))
    def make_salaried(self, new_salary):
        '''
        makes an employee object salaried
        '''
        self.classification = Salaried(new_salary)
    def make_commissioned(self, new_salary, new_rate):
        '''
        makes an employee object commissioned
        '''
        self.classification = Commissioned(new_salary, new_rate)
    def make_hourly(self, hourly_pay):
        '''
        makes an employee object hourly
        '''
        self.classification = Hourly(hourly_pay)


with open('employees.csv', 'r') as emp:
    lines = [line.strip() for line in emp]
employee_list = [line.split(',') for line in lines]



def load_employees():
    '''
    takes the list created from the csv file and should
    return a list of employee objects
    '''
    total_list = []
    hourly_employees = []
    commisioned_employees = []
    salaried_employees = []
    for employee in employee_list:
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
            total_list.append(worker)
            hourly_employees.append((worker.first_name, worker.last_name))
        if classification == '2':
            commission = (employee[8], employee[9])
            worker = Employee(ident, fname, lname, addy, city, state, zipcode, classification, commission)
            total_list.append(worker)
            commisioned_employees.append((worker.first_name, worker.last_name))
        if classification == '1':
            salary = employee[8]
            worker = Employee(ident, fname, lname, addy, city, state, zipcode, classification, salary)
            total_list.append(worker)
            salaried_employees.append((worker.first_name, worker.last_name))

    # final_list.remove(final_list[0])
    return total_list

def find_employee_by_id(ident):
    '''
    finds and returns an employee object based on the id number
    test with 51-4678119
    '''
    for employee in worker_list:
        if str(ident) == employee.emp_id:
            return employee

def process_timecards():
    '''
    adds whatever hours to hourly_rate in Hourly class
    '''
    with open('timecards.csv', 'r') as timecards:
        lines = [line.strip() for line in timecards]
        timecard_list = [line.split(',') for line in lines]
        for timecard in timecard_list:
            id_num = timecard[0]
            actual_time = [float(time) for time in timecard[1:]]
            employee = find_employee_by_id(id_num)
            employee.classification.hourly_record.append(actual_time)

def process_receipts():
    '''
    adds reciepts to reciepts in Commissioned 
    '''
    with open('reciepts.csv', 'r') as reciepts_file:
        lines = [line.strip() for line in reciepts_file]
        reciepts_list = [line.split(',') for line in lines]
        for reciept in reciepts_list:
            id_num = reciept[0]
            reciept_floats = [float(rec) for rec in reciept[1:]]
            employee = find_employee_by_id(id_num)
            employee.classification.receipts.append(reciept_floats)

with open('paylog.txt', 'w'):
    pass

PAY_LOGFILE = 'payroll.txt'

def run_payroll():
    if os.path.exists(PAY_LOGFILE): # pay_log_file is a global variable holding ‘payroll.txt’
        os.remove(PAY_LOGFILE)
    for emp in worker_list: # employees is the global list of Employee objects
        emp.issue_payment() # issue_payment calls a method in the classification
        # object to compute the pay

worker_list = load_employees()
hourly_test = find_employee_by_id('51-4678119')
salary_test = find_employee_by_id('11-0469486')
commission_test = find_employee_by_id('68-9609244')

# print(hourly_test.classification.hourly_rate)
# print(salary_test.classification.salary)
# print(commission_test.classification.commission_pay)

process_timecards()
process_receipts()

print(commission_test.classification.receipts)
commission_test.classification.add_receipt(10)
print(commission_test.classification.receipts)

