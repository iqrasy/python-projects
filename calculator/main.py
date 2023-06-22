# def add(n1, n2):
#     return n1 + n2


# def substract(n1, n2):
#     return n1 - n2


# def multiply(n1, n2):
#     return n1 * n2


# def divide(n1, n2):
#     return n1 / n2


# operations = {"+": add, "-": substract, "*": multiply, "/": divide}

# num1 = int(input("What's the first number?: "))

# for symbols in operations:
#     print(symbols)
# should_continue = True

# while should_continue:
#     op_symbol = input("Pick an operation: ")
#     num2 = int(input("What's the second number?: "))
#     calculation_func = operations[op_symbol]
#     answer = calculation_func(num1, num2)
#     print(f"{num1} {op_symbol} {num2} = {answer}")
#     if input("Type 'y' to continue calculating, or type 'n' to exit.: ").lower() == 'y':
#       num1 = answer
#     else:
#       should_continue = False


def calculate(n1, n2, op):
    if op == '+':
        result = n1 + n2
    elif op == '-':
        result = n1 - n2
    elif op == '*':
        result = n1 * n2
    elif op == '/':
        result = n1 / n2
    elif op == '^':
        result = n1 ** n2
        
    return result
    
first = int(input("Enter first number: "))
op = input("Enter operator: ")
second = int(input("Enter second number: "))
print(first, op, second)
result = calculate(first, second, op)
print('=', result)