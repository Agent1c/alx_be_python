# 1. Simple Calculator with Match Case

num1 = int(input("Enter the first number: ")) # Prompt User for int number Input:
num2 = int(input("Enter the second number: "))

operation = str(input("Choose the operation (+, -, *, /):")) #Calculator operator

#calculator function
match operation:
    case "+":
        print("The result is", num1 + num2)
    case "-":
        print("The result is", num1 - num2)
    case "*":
        print("The result is", num1 * num2)
    case _ if "/":
        try:                                    #Handling the 0 error division
            num1 / num2
        except ZeroDivisionError:
            print("Cannot divide by zero.")
        else:
            print("The result is", num1 / num2)
