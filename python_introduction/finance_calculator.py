# Personal Finance Calculator
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses

#(Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05))
projected_savings = monthly_savings *12 + (monthly_savings * 12 * 0.05)

print(f"Your monthly savings are ${monthly_savings:.1f}")
print(f"Projected savings after one year, with interest, is {projected_savings:.1f}.")


# monthly_savings = (monthly_income- monthly_expenses float(monthly_income)*- float(monthly_expenses))