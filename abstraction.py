from abc import ABC, abstractmethod

# Abstract Base Class (ABC) tanımlama
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

# Concrete class'lar oluşturma
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side
    
    def perimeter(self):
        return 4 * self.side

# Abstract sınıfın kullanımı
# Shape sınıfından türetilmiş nesneler oluşturma
circle = Circle(5)
square = Square(4)

# Her bir şeklin alanını ve çevresini hesaplama
print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())

print("Square Area:", square.area())
print("Square Perimeter:", square.perimeter())





# from abc import ABC, abstractmethod

# class Animal(ABC):
#     family = "Animal"
    
#     # constructor
#     def __init__(self, name, breed, color, gender, size):
#         self.n = name
#         self.b = breed
#         self.c = color
#         self.g = gender
#         self.s = size

#     def __str__(self):
#         return self.n
    
#     @abstractmethod
#     def get_info(self):
#         return self.n, self.b, self.c, self.g, self.s
    
#     @classmethod
#     def get_family(cls):
#         return cls.family
        

# class Dog(Animal):
#     family = "Dog"

#     def get_info(self):
#         return super().get_info()


# class Cat(Animal):
#     family = "Cat"

#     def __init__(self, name, breed, color, gender, size, hairy=True):
#         super().__init__(name, breed, color, gender, size)
#         self.hairy = hairy


#     def get_info(self):
#         return super().get_info(), self.hairy

# class Bird(Animal):
#     pass
#     # def get_info(self):
#     #     return super().get_info()

# # animal1 = Animal("Jack", "African", "White", "Female", "Small")
# # print(animal1)

# cat1 = Cat("Jack", "African", "White", "Female", "Small")
# print(cat1.get_info())

# bird1 = Bird("Jack", "African", "White", "Female", "Small")
# print(bird1)