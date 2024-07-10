class Car:
    def __init__(self, brand, model):
        self.brand = brand  # public attribute
        self.__model = model  # private attribute

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

car = Car("Toyota", "Camry")

print("Car brand:", car.brand)

# print(car.__model) error

print("Car model (via getter):", car.get_model())

car.set_model("Corolla")
print("Updated car model (via setter):", car.get_model())


