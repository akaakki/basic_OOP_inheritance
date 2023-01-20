from animal import Animal

class Dog(Animal):
    
    def __init__(self, number_of_legs: int = 4, number_of_eyes: int = 2):
        super().__init__(number_of_legs, number_of_eyes)

    def breathe(self):
        super().breathe()
        print("Dogs love to breathe with their mouths open.")

    
    def walk(self):
        super().walk()
        print("Dogs love to run.")
