greeting = "hello"
name = "renato"

def greet_2():
    global greeting
    greeting = "goodbye"

    name = "Liron"

    message = f"{greeting}, {name}!"
    print(message)

greet_2()

print(greeting)

print(name)