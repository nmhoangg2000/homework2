items =["T-shirt", "sweater"]
while True:
    cmd = input("Welcome to our shop, what do you want(C, R, U, D)? ").upper()
    if cmd == "R":
        print("our items: ",end=" ")
        print(items, sep=", ")
    if cmd == "C":
        n = input("enter new items: ")
        items.append(n)
        print(items, sep=", ")    
    elif cmd == "U":
        n = input("update items: ")
        a = int(input("update position? "))
        items[a-1] = n
        print("Our items: ", end = "")
        print(items,sep=", ")
    elif cmd == "D":
        i = int(input("delete position: "))
        items.pop(i-1)
        print("Our items: ", end = "")
        print(items)
    elif cmd == "E":
        break