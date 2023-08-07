
#for x in "Python":
#   print(x)

#for x in ['a', 'b', 'c']:
#   print(x)

#for x in range(5):
#   print(x)

#for x in range(0, 10, 2):
#    print(x)

#print(type(range(50000000)))
#print([1, 2, 3, 4, 5])

"""names = ["AJohn", "Mary"]
found = False
for name in names:
    if name.startswith("J"):
        print("Found")
        found = True
        break

if not found:
    print("Not found")"""

names = ["AJohn", "Mary"]
for name in names:
    if name.startswith("J"):
        print("Found")
        break
else:
    print("Not found")