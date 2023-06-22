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