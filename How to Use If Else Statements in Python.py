"""a = int(input("Write a number for var a: \n"))
b = int(input("Other one for var b pliiiis b0000s:\n"))

if a < b:
    print("a is less than b")
else:
    print("a is bigger than b")



a = int(input("Write a number for var a: \n"))
b = int(input("Other one for var b pliiiis b0000s:\n"))

if a < b:
    print("a is smaller than b")
elif a==b:# elif adds a condition
    print("a is equal to b")
elif a > b +20:
    print("a is bigger than b + 20")
else:
    print("b is bigger than a")


a = int(input("Write a number for var a: \n"))
b = int(input("Other one for var b pliiiis b0000s:\n"))

if a < b:
    print("a is smaller than b")
else:
    if b > a:
        print("b is bigger than a")
    else:
        print("a is equal to b")

"""

#bmi calculator

height = float(input("Persons height in meters"))
weight = float(input("Persons wheight in kilograms"))

bmi = weight / (height ** 2) #the double * means to the power of

print("BMI: ", bmi)
if bmi < 25:
    print("Is not overweight")
else:
    print("The person is overweitht")