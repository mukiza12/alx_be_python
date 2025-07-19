#basic calculator
while True:
   nummber1 = 10
   nummber2 = 5
   operations = input("Enter your operator here: \n (*, -, /, %, +)")

#Error handling: If the user enter invalid number the program won't continue to be excuted using while loop in
#  case the user fails, then the program does exit direclty
   try:
    numint_1 = float(number1)
    numint_2 = float(number2)
   except ValueError:
        print("Invalid input: Please Entr a number: \n")
        continue
    #loop will continue until the user input the corect number
   print(f"ok coreect {numint_1} and {numint_2}")
   


   if operations == "*":
     multiplication = numint_1 * numint_2
     print(f"Multiplication is: {multiplication}")
   elif operations == "/":
     if numint_2 == 0:
      print(f"Maths error")
     else: 
       quotient = numint_1 / numint_2
     print(f"the quotient i :{quotient} ")
   elif operations == "-":
    difference = numint_1 - numint_2
    print(f"the difference is: {difference}")

   elif operations == "+":
    addition = numint_1 + numint_2
    print(f"the addition is: {addition}")
   elif operations == "%":
     modulus = numint_1 % numint_2
     print(f"the modulus is: {modulus}")
   else: 
    print("invalid input: please choose from *, %, -, +, /")
   another_calculation = input("chose yes or no: \n").lower()
   if another_calculation != "yes":
     print("Thank you for using the calculator! Goodbye.")
     break 
   
     
  




