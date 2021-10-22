f = open("test.txt")
line = f.readlines()
for x in line:
    print(x)

name = "My name is pranav, I am 13 years old"
words = name.split(",")
print(words)

def greet(name):
    print("Hello " + name + ". How are you?")

greet("Pranav")