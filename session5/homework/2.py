prices ={
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
total = 0

for fruits in prices:
    print(fruits)
    print("price:", prices[fruits])
    for a in stock:
        if fruits == a:
            print("stock:", stock[a])
            print()
            sold = prices[fruits] * stock[a]
            total += sold
print(total)
