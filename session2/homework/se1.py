h = int(input("Height:"))
w = int(input("weight:"))
h = h*0.01
BMI = w/(h*h)
print("BMI")

if BMI < 16:
    print("severly underweight")
elif BMI < 18.5:
    print("underweight")
elif BMI < 25:
    print("normal")
elif BMI < 30:
    print("overweight")
else:
    print("Obese")                
