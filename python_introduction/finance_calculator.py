
#finance calculator
while True:
    income = input("Enter your monthly income: \n")
    expenses = input("Enter your total monthly expenses: \n")
    try:
        expenses_i = int(expenses)
        income_i = int(income)
    except ValueError:
            print("invalid input")
            continue
    print(" ok lets continue")
    
    savings =  income_i - expenses_i


    Projected_Savings = savings * 12 + (savings * 12 * 0.05)

    print(f"Your monthly savings are ${savings}")

    print(f"Projected savings after one year, with interest, is: $p{Projected_Savings}.")
    print(f"Projected savings after one year, with interest, is: ${Projected_Savings}.")

    user_input = input('do you want to continue, yes or no?: \n').lower()
    if user_input != "yes":
        print('Thank you goodbye!')
        break


