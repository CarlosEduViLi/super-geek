a = 1 
b = 2

print(a + b)

if a < b:
    print("a is less than b")
else:
    print("a is not less than b")

for i in range(5):
    print(i)

def add(x, y):
    return x + y
result = add(a, b)
print("The sum of a and b is:", result)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
p = Person("Alice", 30)
p.greet()

try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero!")
import math
print("The square root of 16 is:", math.sqrt(16))