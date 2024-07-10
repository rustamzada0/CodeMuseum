class MyClass:
    class_variable = 0

    def __init__(self, value):
        self.instance_variable = value

    @staticmethod
    def static_method():
        print("This is a static method")

    def display(self):
        print(f"Instance Variable: {self.instance_variable}, Class Variable: {MyClass.class_variable}")

# Create instances of MyClass
obj1 = MyClass(10)
obj2 = MyClass(20)

# Call static method
MyClass.static_method()  # This is a static method
obj1.static_method()     # This is a static method
obj2.static_method()     # This is a static method

obj1.display()  # Instance Variable: 10, Class Variable: 0
obj2.display()  # Instance Variable: 20, Class Variable: 0
