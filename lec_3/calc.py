 #Variant 1

def mycalculator(exp):
    try:
        operators = ["+", "-", "*", "/"]
        operator = None

        for op in operators:
            if op in exp:
                operator = op
                break
        if operator is None:
                return "Unsupported operator or invalid expression"

        num1, num2 = map(float, exp.split(operator))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                return "Division by zero is not allowed"
            result = num1 / num2

        return result

    except ValueError:
        return "Please enter valid numbers."
    
user_input = input("Enter an expression: ")
result = mycalculator(user_input)
print(f"Result is : {result}")



#Variant 2

num1 = float(input("Enter first number: "))
op = (input("Enter operator: "))
num2 = float(input("Enter second number:" ))

if op == "+":
    print(num1 + num2)
elif op == "_":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")
