import art

print(art.logo)


def add(n1, n2):
    """ Takes n1 and adds n2 to it"""
    return n1 + n2

def subtract(n1, n2):
    """Takes n1 and subtracts n2 from it"""
    return n1 - n2

def multiply(n1, n2):
    """Takes n1 and multiplies n2 to it"""
    return n1 * n2

def divide(n1, n2):
    """Takes n1 and divides n2 from it"""
    return n1 /n2

# A dictionary with operation symbols as keys to reference the functions above
operations = {"+": add, "-": subtract, "*": multiply, "/" : divide}

calculator_on = True
keep_result = 'n'
result = None

while calculator_on:
    # for the first loop it automatically go to the else
    if keep_result == 'y':
        first_number = result
    else:
        first_number =  float(input("Whats the first number?: "))
    for op in operations:
        print(op)
    operation = input("Pick an operation: ")
    second_number = float(input("What's the next number?: "))
    result = operations[operation](first_number,second_number)
    print(f"{first_number} {operation} {second_number} = {result}")

    keep_result = input("Type 'y' to continue calculating with {result), or type 'n' to start a new calculation: ")