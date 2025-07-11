#149
def items(*args):
    print(*args)

items("Cheese","Chocolate","Mushroom","Beef")
items("Nigga","Black","Asep")

def build_user(first,last,**kwargs):
    kwargs["first"] = first
    kwargs["last"] = last
    print(kwargs)

build_user("Ronaldo","Wati",Location = "Jakarta", Country = "Indonesia" )
#print(user)
