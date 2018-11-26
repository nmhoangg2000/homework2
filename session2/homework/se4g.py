import sys
m = int(input("enter a number:"))
n = int(input("enter a number:"))
for i in range(m):
    for j in range(n):
        sys.stdout.write("*")
    print()        