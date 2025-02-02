def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y if y != 0 else "Error: Division by zero"

print("Simple Calculator")
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == '+':
    print("Result:", add(x, y))
elif operation == '-':
    print("Result:", subtract(x, y))
elif operation == '*':
    print("Result:", multiply(x, y))
elif operation == '/':
    print("Result:", divide(x, y))
else:
    print("Invalid operation")