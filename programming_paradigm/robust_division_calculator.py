def safe_divide(numerator, denominator):

    try:
        result = (numerator) / (denominator)
    except ZeroDivisionError as e:
        print("{e}")
        
    except ValueError as e:
        print("Error: Please enter numeric values only.")
    else:
        print(f"The result of the division is {result}")