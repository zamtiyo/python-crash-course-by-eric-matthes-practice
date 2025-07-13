#Restaurant
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

#User
#hal 162
class User:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"The first name of the user is {self.first_name} the last name is {self.last_name}")

    def greet_user(self):
        print(f"hello {self.first_name} {self.last_name}")

user_1 = User("Bian","Nigga")
user_1.describe_user()
user_1.greet_user()

user_2 = User("Oop","Anjing")
user_2.describe_user()
user_2.greet_user()
