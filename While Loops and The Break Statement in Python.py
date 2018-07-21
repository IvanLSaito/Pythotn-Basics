list = [5, 6, 8, 10, 20]

total = 0
i = 0

#len = .size or .length
while i < len(list) and list[i] > 0:
    total = total + list[i]
    i += 1
print(total)

list2 = [5, 6, 8, 10, 20, -9, -87, -100]
total = 0
for number in list2:
    if  number <= 0:
        break
    total = number + total
print(total)