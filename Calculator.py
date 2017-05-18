print("Welcome to the Basic Calculator!")
number1=(int(input("Please enter your First Number")))
number2=(int(input("Please enter your Second Number")))

choice=input("Would you like to Add, Subtract, Multiply or Divide? (Use Symbols)")


if choice == "+":
    answer1 = number1+number2
    print (answer1)

elif choice == "-":
    answer2 = number1-number2
    print (answer2)

elif choice == "x":
    answer3 = number1*number2
    print (answer3)

elif choice == "÷":
    answer4 = number1/number2
    print (answer4)

else:
    print("ERROR")
