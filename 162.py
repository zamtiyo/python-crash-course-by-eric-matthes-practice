class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):              
        print(f"The name of the restaurant is {self.name.title()}!")
        print(f"{self.name.title()} makes {self.cuisine_type.title()} food!")

    def open_restaurant(self):                  
        print(f"{self.name.title()} is open!")
        print("\n")

r2 = Restaurant('taco bell', 'mexican')         
r2.describe_restaurant()
r2.open_restaurant()

