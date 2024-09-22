# Draw the Pattern

# prompt the user input
size = int(input("Enter the size of the pattern: "))
row = 0

while row < size:
    for col in range(size):
        print("*", end="")  # Print asterisk without advancing to a new line
    print()  
    row += 1  # Increment the row counter
