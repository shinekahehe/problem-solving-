def calculator():
    num1 = int(input("Enter the first number: "))
    operator = input("Enter an operator (+, -, *, /): ")
    num2 = int(input("Enter the second number: "))
    if operator == "+":
        result = num1 + num2
        print("The result is:",result)
    elif operator == "-":
        result = num1 - num2
        print("The result is:",result)
    elif operator == "*":
        result = num1 * num2
        print("The result is:",result)
    elif operator == "/":
            result = num1 / num2
            print("The result is:",result)
calculator()
