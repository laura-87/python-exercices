def increment(number: int, by: int = 1) -> tuple[int, int]:
    return number, number + by


print(increment(2))


# Arguments xargs

def multiply(*list):
    total = 1
    for number in list:
        total *= number
    return total


print(multiply(2, 3, 4, 5))


# Arguments xxargs

def save_user(**user):
    print(user["id"])
    print(user["name"])


save_user(id=1, name="admin")
