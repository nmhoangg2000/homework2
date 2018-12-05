print("Answer the following algebra question: ")
print("If x = 8, then what is the value of 4(x + 3) ?")
a = [35, 36, 40, 44]
for i in range(len(a)):
    print(i +1, a[i], sep=" ")
choice = int(input("your choice: "))
if choice == 4:
    print("bingo")
else:
    print(":(")   
