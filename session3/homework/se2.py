while True:
    a = int(input("Guess my number(1-100)?"))

    if a < 22:
        print("too small")    
    elif a == 22:
        print("bingo")
        break
    else:
        print("too large")      