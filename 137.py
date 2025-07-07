#137
def make_shirt(size="large", message="I love python"):
    print(f"The size of your t shirt is {size}")
    print(f"The message is {message}")
#Ini contoh dari positional argumen
#make_shirt(9)
#ini contoh dari keyword argumen
#make_shirt(size=8)

make_shirt(size="Medium")
make_shirt(size="Large")
make_shirt(message="I hate niggers")

def describe_city(city,country="indonesia"):
    print(f"{city} is in {country}")
describe_city("Ngawi")
describe_city("Yogyakarta")
describe_city("California love", country="USA")
