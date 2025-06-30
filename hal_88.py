users = []
if users:
    for user in users:
        if user == "admin":
            print("Hello admin, would you like to see the status report?")
        else:
            print(f"Hello {user}")
else:
    print("We need to find some users!")
