def safe_divide(numerator, denominator):
    try:
        numerator = int(numerator)
        denominator = int(denominator)
        result = numerator / denominator

    except ZeroDivisionError as e:
        print("Error: Cannot divide by zero.")  
  
    except ValueError as e:
        print("Error: Please enter numeric values only.")
    else:
        print(result)