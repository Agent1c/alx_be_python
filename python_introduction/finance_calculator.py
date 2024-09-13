# Personal Finance Calculator
monthly_income = int(input("Enter your monthly income: "))
monthly_expense = float(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expense
print(f"Your monthly savings are {monthly_savings}")

#(Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05))

projected_savings = monthly_savings * 12 + (monthly_savings * 12 *0.05) #With A simple annual interest rate of 5%.

print(f"Projected savings after one year, with interest, is {projected_savings}")