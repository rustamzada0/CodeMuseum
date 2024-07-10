class Employee:
    # Class variable or attribute
    company_name = "Tech Corp"
    raise_amount = 1.05
    
    def __init__(self, first_name, last_name, salary):
        # Instance variables
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    # Instance method
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    # Instance method
    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)
    
    # Class method
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    
    # Static method
    @staticmethod
    def is_workday(day):
        return day.weekday() < 5

# Object creation
emp1 = Employee("John", "Doe", 50000)
emp2 = Employee("Jane", "Smith", 60000)

# Accessing instance variables
print(emp1.full_name())  # Output: John Doe
print(emp2.full_name())  # Output: Jane Smith

# Accessing class variables
print(Employee.company_name)  # Output: Tech Corp

# Applying raise
emp1.apply_raise()
print(emp1.salary)  # Output: 52500 (assuming raise_amount is 1.05)

# Using class method to change raise amount
Employee.set_raise_amount(1.10)
emp2.apply_raise()
print(emp2.salary)  # Output: 66000 (assuming raise_amount is 1.10)

# Using static method
import datetime
my_date = datetime.date(2023, 7, 5)
print(Employee.is_workday(my_date))  # Output: True (if it's a weekday)
