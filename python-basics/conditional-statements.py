
age = 22
if age >= 18:
    print("adult")
    print("adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

print("All done!")

if 1 == "a":
    pass
else:
    pass


# Logical Operators


name = ""
if not name.strip():
    print("Name is empty")

age = 22
if age >= 18 and age < 65:
    print("Eligible")

# 18 <= age > 65 chaining comparison operator

#Ternary Operator

age = 22
if age >= 18:
    message = "Eligible"
else:
    message = "Not eligible"

message = "Eligible" if age >= 18 else "Not eligible"

print(message)

