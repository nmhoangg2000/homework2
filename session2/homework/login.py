print(" Welcome bro ")

user = input("Username: ")
if user != "c4e":
    print("You are not superuser")
    exit()

pas = input("Password: ")
if pas != "code4change":
    print("Password is incorrect. Try again")
else:
    print("Welcome") 