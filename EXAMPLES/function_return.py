def get_hello():
    return "Hello, world"

h = get_hello() 
print(f"{h = }")

def hello():
    print("Hello, world")

h = hello()
print(f"{h = }")

def double(x):
    return x * 2

d = double(10)
print(f"{d = }")

def doit(a,b):
    print(f"{a = }, {b = }")

doit(10, 20)
doit('spam', 'eggs')