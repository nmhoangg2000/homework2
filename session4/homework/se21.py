# 2.5
print("hello, my name is Hoàng and these are my sheep sizes")
size = [5, 7, 300, 90, 24, 50, 75]
print(size)

for i in range(4):
    print("month", str(i +1))

    print("one month has passed, here is my flock")
    for j in range(len(size)):
        size[i]= size[i] + 50
    print(size)
    
    n = max(size)
    print("Now my biggest sheep has size", n, "let's shear it")
    
    print("after shearing here is my flock")
    index = size.index(n)
    size[index] = 8
    print(size)
   
# 2.6
size_sum = sum(size)
print("My flock has sizes in total: ", size_sum)
money = size_sum * 2
print("I would get ", size_sum, end = " * 2$ = ")
print(money)