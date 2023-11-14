class Fruit:
    def __init__(self, name, color, taste):
        self.name = name
        self.color = color
        self.taste = taste

    def describe(self):
        return f"This is a {self.color} {self.name} with a {self.taste} taste."
    
class Apple(Fruit):
    def __init__(self, name, color, taste, variety):
        super().__init__(name, color, taste)
        self.variety = variety

    def describe(self):
        return f"This is a {self.color} {self.variety} apple with a {self.taste} taste."

fruit1 = Fruit("Banana", "yellow", "sweet")
fruit2 = Fruit("Orange", "orange", "citrusy")

print(fruit1.describe())  
print(fruit2.describe()) 

apple1 = Apple("Apple", "red", "crisp", "Fuji")
apple2 = Apple("Apple", "green", "tart", "Granny Smith")

print(apple1.describe()) 
print(apple2.describe())  
