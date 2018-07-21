"""
a collection of instructions/code
function
"""
"""
def function():
    print("Hellooo")
    print("bukabuka")

function()

def secondFunction(x):
    return  5*x

number = int(input("Insert a number\n"))
result = secondFunction(number)
print(result)

def thirdFunction(x, y):
    return x + y
number = int(input("Insert a number\n"))
result = thirdFunction(number, 90)
print(result)
"""

#BMI calculator

def BMI(heightCm, weightKg):
    bmi = weightKg / (heightCm ** 2)
    print( "BMI: ", bmi)
    if bmi < 25:
        print("Not overweight")
    else:
        print("overweight")

height = 190
weight = 87

BMI(height, weight)