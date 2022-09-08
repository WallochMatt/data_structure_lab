#Set
class FruitBasket:
    def __init__(self):
        self.fruits = {"Banana", "Blueberry", "Raspberry", "Pear", "Orange"}

    def add_fruit(self, more_fruit):
        """
        Parameter:
        more_fruit : str -> string is added to the set
        """
        self.fruits.add({more_fruit})


    def display_fruits(self):
        for fruit in self.fruits:
            print(fruit)
