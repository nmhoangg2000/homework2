# 2.1
print("hello, my name is Hoàng and these are my sheep sizes")
size = [5, 7, 300, 90, 24, 50, 75]
print(size)
# 2.2
n = max(size)
print("Now my biggest sheep has size", n, "let's shear it")
# 2.3
print("after shearing here is my flock")
index = size.index(n)
size[index] = 8
print(size)
# 2.4
print("one month has passed, here is my flock")
for i in range(len(size)):
    size[i]= size[i] + 50
print(size)   

 
