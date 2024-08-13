# getter
# setter
# property

class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    @property
    def name(self):
        print(self.__name)
    
    # @name.getter
    # def name(self):
    #     return self.__name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and new_name.strip():
            self.__name = new_name
        else:
            raise ValueError("Ad düzgün deyil.")

    @name.deleter
    def name(self):
        del self.__name

    @property
    def salary(self):
        print(self.__salary)
    
    # @salary.getter
    # def salary(self):
    #     return self.__salary
    
    @salary.setter
    def salary(self, new_salary):
        if new_salary >= 0:
            self.__salary = new_salary
        else:
            raise ValueError("Maaş mənfi ola bilməz.")
        self.__salary = new_salary

    @salary.deleter
    def salary(self):
        del self.__salary


emp1 = Employee("Farid", 999)

emp1.name # Farid
emp1.name = "Tunay"
emp1.name # Tunay

print("_____________________________________________________________")
print()

emp1.salary
emp1.salary = 1000
emp1.salary

del emp1.name
emp1.name # Error

# emp1.__salary = 1000 access yoxdur





