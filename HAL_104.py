#hal 104
person = {"First_Name": "Anjing", "Last_Name": "Sigma", "Age": "100", "City": "ngawi", "Kota": "Ngawi"}
for kontol, ngentod in person.items():
    print(f"{kontol}: {ngentod.title()}")

print(f"\n{person['First_Name'].title()}")

rivers = {" nile": " egypt", " amazon": " brazil", " yangtze": " nigeria"}
for river,country in rivers.items():
    print(f"As the{river.title()} runs through{country.title()}")

for bangsat in rivers.keys():
    print(bangsat.title())

for country in rivers.values():
    print(country.title())




