message = "a"

def greet():
    #Este global es una muy mala práctica
    #global message
    message = "b"

greet()
print(message)