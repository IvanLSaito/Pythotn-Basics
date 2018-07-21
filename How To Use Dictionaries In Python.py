
d = {"John": 22, "Freddy": 33}

#square brackets = key
d["Santa"] = 999

print(d["John"])

"""keys are commonly strings or numbers"""
d[10] = 100

"""Key and value reserved words for key and value in a dictionary"""
for key, value in d.items():
    print("Key: ", key, " Value: ", value)