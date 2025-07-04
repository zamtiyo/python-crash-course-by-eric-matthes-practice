sandwich_orders = ["Tuna", "Cheese", "Chocolate", "Pastrami", "Egg", "Pastrami", "Pastrami"]
finished_sandwiches = []

print("Sorry, the deli has run out of pastrami.")

while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(sandwich)

