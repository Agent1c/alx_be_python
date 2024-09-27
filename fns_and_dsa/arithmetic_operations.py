"""a function that performs basic arithmetic operations"""
def perform_operation(num1, num2, operation):
 
    #Evaluating the operation function based on the user input/request
    if operation == "add":
        return add(num1, num2)
    elif operation == "subtract":
        return subtract(num1, num2)
    elif operation == "multiply":
        return multiply(num1, num2)
    elif operation == "divide":
        return divide(num1, num2)
    else:
        print("Invalid operation, Please try again.")

#Arithmetics Functions lining from "+", "-", " * " & " / "
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    try:    #Controlling Zero division error, returning it
        num1 / num2
    except ZeroDivisionError:
        print("Cannot Divide by Zero.")
    else:
        return num1 / num2
    perform_operation(num1, num2)