# Day 4 - Python Functions

# 1 simple function
def say_hello():
    print("Hello Python")

say_hello()


# 2 function with parameter
def greet(name):
    print("Hello", name)

greet("Alice")
greet("Bob")


# 3 add numbers
def add(a, b):
    return a + b

result = add(5, 7)
print("Result:", result)


# 4 dictionary example
student = {
    "name": "Tom",
    "age": 21
}

def show_student(data):
    print("Name:", data["name"])
    print("Age:", data["age"])

show_student(student)
