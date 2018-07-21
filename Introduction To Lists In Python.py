"""
a = [3, 10, -1]
print(a)

#.apend add data to the list

a.append(22)
print(a)

#you can mix types of data in a list

a.append("hola que tal")
print(a)

b = ["a", "b"]

a.append(b)
#you can add other lists to an existence list

print(a)

a.pop()
print(a)
#.pop deletes the last item in the list
a.pop()
print(a)

#adding to a var a specific position of the list
var = a[0]
print(var)

#change a position of the list
a[0] = "hola"
print(a)
"""

#canging pos 0 to pos 2
c = [1, 2, 3]
aux1 = c[0]
aux2 = c[2]
c[0] = aux2
c[2] = aux1
print(c)

c = [1, 2, 3]
c[0], c[2] = c[2], c[0]
print(c)

