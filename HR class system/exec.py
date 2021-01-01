import hr
import employees
import productivity


'''
The program creates three employee objects, one for each of the derived classes.
Then, it creates the payroll system and passes a list of the employees to its .calculate_payroll() method,
which calculates the payroll for each employee and prints the results.
Notice how the Employee base class doesn’t define a .calculate_payroll() method.
This means that if you were to create a plain Employee object and pass it to the PayrollSystem, then you’d get an error. 
'''

manager = employees.Manager(1, 'Mary Poppins', 3000)
secretary = employees.Secretary(2, 'John Smith', 1500)
sales_guy = employees.SalesPerson(3, 'Kevin Bacon', 1000, 250)
factory_worker = employees.FactoryWorker(2, 'Jane Doe', 40, 15)
employees = [
    manager,
    secretary,
    sales_guy,
    factory_worker,
]
productivity_system = productivity.ProductivitySystem()
productivity_system.track(employees, 40)
payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll(employees)

'''
Calculating Payroll
===================
Payroll for: 1 - John Smith
- Check amount: 1500

Payroll for: 2 - Jane Doe
- Check amount: 600

Payroll for: 3 - Kevin Bacon
- Check amount: 1250
'''
