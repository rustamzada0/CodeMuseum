class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Bark!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Duck(Animal):
    def speak(self):
        return "Quack!"

# Polimorfizm
def animal_speaks(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()
duck = Duck()

animal_speaks(dog)   # Output: Bark!
animal_speaks(cat)   # Output: Meow!
animal_speaks(duck)  # Output: Quack!
