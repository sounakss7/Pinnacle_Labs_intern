def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x//y if y != 0 else "Error: Division by zero"
print("Available operations:")
operation=input("Enter the operation (+, -, *, /): ")

if operation == "+":
    print("RESULT:",add(float(input("Enter the first number: ")), float(input("Enter the second number"))))
elif operation == "-":
    print("RESULT:",subtract(float(input("Enter the first number: ")), float(input("Enter the second number"))))
elif operation == "*":
    print("RESULT:",multiply(float(input("Enter the first number: ")), float(input("Enter the second number"))))
elif operation == "/":
    print("RESULT:",divide(float(input("Enter the first number: ")), float(input("Enter the second number"))))


