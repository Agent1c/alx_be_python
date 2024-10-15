class Calculator:
    calculation_type = "Arithmetic Operations" # A class attribute  with a value of multiply

    """static method , with a  addition method that returns the value of 'a, b'"""
    @staticmethod
    def add(a, b):
        return a + b
    
    """class method , with a  multiplication method that returns the value of 'a, b'"""
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b