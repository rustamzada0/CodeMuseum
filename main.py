def feed_lion():
    print("Feeding the lion")

def feed_tiger():
    print("Feeding the tiger")

def feed_animal(animal):
    if animal == "lion":
        feed_lion()
    elif animal == "tiger":
        feed_tiger()
    else:
        print("Unknown animal")

# Usage
feed_animal("lion")
feed_animal("tiger")

# Yeni heyvan elave elesey kodu deyismeliyik ve yeni funksiya elave elemeliyik
# Ayrıca, hayvanların özelliklerini ve davranışlarını yönetmek zor olabilir.

class Animal:
    def feed(self):
        raise NotImplementedError("This method should be overridden in subclasses")

class Lion(Animal):
    def feed(self):
        print("Feeding the lion")

class Tiger(Animal):
    def feed(self):
        print("Feeding the tiger")

# Usage
lion = Lion()
lion.feed()

tiger = Tiger()
tiger.feed()
