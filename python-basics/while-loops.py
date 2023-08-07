guess = 0
answer = 5

while answer != guess:
    guess = int(input("Guess: "))
    if guess == 4:
        break
else:
    print("else")