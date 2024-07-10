class MyClass:
    class_variable = 0

    def __init__(self, value):
        self.instance_variable = value

    @classmethod
    def increment_class_variable(cls):
        cls.class_variable += 1

    @classmethod
    def set_class_variable(cls, value):
        cls.class_variable = value

    def display(self):
        print(f"Instance Variable: {self.instance_variable}, Class Variable: {MyClass.class_variable}")

# Create instances of MyClass
obj1 = MyClass(10)
obj2 = MyClass(20)

# Call class method
MyClass.increment_class_variable()
MyClass.increment_class_variable()

obj1.display()  # Instance Variable: 10, Class Variable: 2
obj2.display()  # Instance Variable: 20, Class Variable: 2

MyClass.set_class_variable(5)
obj1.display()  # Instance Variable: 10, Class Variable: 5
obj2.display()  # Instance Variable: 20, Class Variable: 5
