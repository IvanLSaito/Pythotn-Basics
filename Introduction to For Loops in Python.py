a = [1 , 2, 3]
#for each loop
for number in a:
    print(number)

print("\n")
sum = 0
for number in a:
    sum = sum + number
    print(number)
    print("Total at the time: ", sum)

#range types the values in between ex: range(1,5) = 1, 2 , 3 , 4
b = list(range(0,11))
print(b)
print("\n")
sum = 0
for number in range(0, 6):
    sum = sum + number
    print(number)
    print("Total at the time: ", sum)

print("\n")

#sum of multiples of 3

sum = 0
for number in range(0,8):
    if number % 3 == 0:
        sum = sum + number
print(sum)


# sum of multiples 3 and 5 that ar less than 100
sum = 0
sum2 = 0
for number in range(0, 101):
    if number % 3 == 0:
        sum = sum + number
    elif number % 5 == 0:
        sum2 = sum2 + number
print("Sum of multiples of 3: ", sum)
print("Sum of multiples of 5: ",  sum2)