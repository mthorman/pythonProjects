# building a better calculator

num1 = float(input("Enter first number: ")) # converts user input to float
op = input("Enter operator: ") # addition, subtraction, division, etc
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1/num2)
elif op == "*":
    print(num1*num2)
else:
    print("Invalid operator")
