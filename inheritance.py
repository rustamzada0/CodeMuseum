class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def calculate_pay(self):
        return self.salary


class Manager(Employee):
    def __init__(self, first_name, last_name, salary, bonus):
        super().__init__(first_name, last_name, salary)
        self.bonus = bonus

    def calculate_pay(self):
        base_pay = super().calculate_pay()
        return base_pay + self.bonus


class Developer(Employee):
    def __init__(self, first_name, last_name, salary, programming_language):
        super().__init__(first_name, last_name, salary)
        self.programming_language = programming_language

    def get_language(self):
        return self.programming_language


emp1 = Employee("John", "Doe", 50000)
print(emp1.full_name())  # Output: John Doe
print(emp1.calculate_pay())  # Output: 50000

manager1 = Manager("Jane", "Smith", 60000, 10000)
print(manager1.full_name())  # Output: Jane Smith
print(manager1.calculate_pay())  # Output: 70000 (60000 + 10000)

dev1 = Developer("Mike", "Johnson", 55000, "Python")
print(dev1.full_name())  # Output: Mike Johnson
print(dev1.calculate_pay())  # Output: 55000
print(dev1.get_language())  # Output: Python
