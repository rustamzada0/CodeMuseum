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
