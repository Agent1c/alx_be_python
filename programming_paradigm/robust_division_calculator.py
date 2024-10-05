def safe_divide(numerator, denominator):
    try:
        """User inputs prompt responds"""
        numerator = float(numerator), denominator = float(denominator)
        result = numerator / denominator
        """ZeroDivision and ValueError handlers"""
    except ZeroDivisionError as e:
        return "Error: Cannot divide by zero."
  
    except ValueError as e:
        return "Error: Please enter numeric values only."
    else:
        return (f"The result of the division is {result}") #Returning users input results
