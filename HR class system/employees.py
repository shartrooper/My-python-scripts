
from abc import ABC, abstractmethod

'''
The Employee class in is what is called an abstract base class.
Abstract base classes exist to be inherited, but never instantiated. 
'''
class Employee(ABC):
    def __init__(self, id, name):
        self.id = id
        self.name = name
    @abstractmethod
    def calculate_payroll(self):
        pass

'''
You derive Employee from ABC, making it an abstract base class.
Then, you decorate the .calculate_payroll()
method with the @abstractmethod decorator.

This change has two nice side-effects:
    You’re telling users of the module that objects of type Employee can’t be created.
    You’re telling other developers working on the hr module that if they derive from Employee,
    then they must override the .calculate_payroll() abstract method.
'''

'''
Classes that inherit from Employee
'''

class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary

class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate

class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission
#Interface class. Doesn't inherit anything from Employee, yet It has the same atributtes and method
class DisgruntledEmployee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def calculate_payroll(self):
        return 1000000

class Manager(SalaryEmployee):
    def work(self, hours):
        print(f'{self.name} screams and yells for {hours} hours.')

class Secretary(SalaryEmployee):
    def work(self, hours):
        print(f'{self.name} expends {hours} hours doing office paperwork.')

class SalesPerson(CommissionEmployee):
    def work(self, hours):
        print(f'{self.name} expends {hours} hours on the phone.')

class FactoryWorker(HourlyEmployee):
    def work(self, hours):
        print(f'{self.name} manufactures gadgets for {hours} hours.')
