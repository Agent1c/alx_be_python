"""a function that performs basic arithmetic operations"""
def perform_operation(num1, num2, operation):
 
    #Evaluating the operation function based on the user input/request
    if operation == "add":
        return add(num1, num2)
    elif operation == "subtract":
        return subtract(num1, num2)
    elif operation == "multiply":
        return multiply(num1, num2)
    elif operation == 'divide':
        if num2 == 0:
            print("Undefined")
    else:
        result = num1/num2
        print(result)

        # Controlling Zero division error, returning it
    #     try:
    #         return num1 / num2
    #     except ZeroDivisionError:
    #         return f"Error: Division by zero is not allowed."
    # else:
    #     print("Error: Invalid operation. Please use 'add', 'subtract', 'multiply', or 'divide'.")



    #Arithmetics Functions lining from "+", "-", " * " & " / "
    # def add(num1, num2):
    #     return num1 + num2

    # def subtract(num1, num2):
    #     return num1 - num2

    # def multiply(num1, num2):
    #     return num1 * num2

    # def divide(num1, num2):
    #     return num1 / num2

    print(perform_operation(num1, num2, operation))