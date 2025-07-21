age = input("How old are you?: \n")
age_i = int(age)

new_age = age_i + 27

print(f"In 2050, you will be {new_age} years old.")

#finance calculator
income = input("Enter your monthly income: \n")
expenses = input("Enter your total monthly expenses: \n")

expenses_i = int(expenses)
income_i = int(income)


savings =  income_i - expenses_i


Projected_Savings = savings * 12 + (savings * 12 * 0.05)

print(f"Your monthly savings are ${savings}")
print(f"Projected savings after one year, with interest, is: $p{Projected_Savings}.")