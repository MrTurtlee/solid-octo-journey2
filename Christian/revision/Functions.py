operater = input("Do you want to add, minus, divide or multiply")
num1 = input("What is your first number?")
num2 = input("What is your second number?")

def addition(num1, num2):
    answer = int(num1) + int(num2)
    return answer

def minus(num1, num2):
    answer = int(num1) - int(num2)
    return answer

def divide(num1, num2):
    answer = int(num1) / int(num2)
    return answer

def multiply(num1, num2):
    answer = int(num1) * int(num2)
    return answer

if operater == "add":
    print(addition(num1,num2))
if operater == "minus":
    print(minus)
if operater == "divide":
    print(divide)
if operater == "multiply":
    print(multiply)