#A simple Program that automically adds the variable on at the start of the calculation in the same unit
def variable(x):
    x = (int(x))
    x = x**2
    xword = (str(x))
    print(xword+" is your Variable!!")                                  
    print("Now we will move onto the calculating unit")                               
    number1=(int(input("Please enter your First Number")))
    number2=(int(input("Please enter your Second Number")))


    choice=input("Would you like to Add, Subtract, Multiply or Divide? (Use Symbols)")


    if choice == "+":
        answer1 = x+number1+number2
        print (answer1)

    elif choice == "-":
        answer2 = x-number1-number2
        print (answer2)

    elif choice == "x":
        answer3 = x*number1*number2
        print (answer3)

    elif choice == "÷":
        answer4 = x/number1/number2
        print (answer4)

    else:
        print("ERROR")







variable2=(input("Please enter your Variable"))

variable(variable2)
