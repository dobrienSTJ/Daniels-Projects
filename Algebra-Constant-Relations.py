#Automattically multiplies constant by variable  e.g 2(3)
def variable(x,y):
    print(x+" is your Variable!!")
    print(y+" is your Constant!!")
    print("Now we will move onto the calculating unit")                               
    x = (int(x))
    y = (int(y))
    number1=(int(input("Please enter your First Number")))
    number2=(int(input("Please enter your Second Number")))


    choice=input("Would you like to Add, Subtract, Multiply or Divide? (Use Symbols)")


    if choice == "+":
        answer1 = y*x+number1+number2
        print (answer1)

    elif choice == "-":
        answer2 = y*x-number1-number2
        print (answer2)

    elif choice == "x":
        answer3 = y*x*number1*number2
        print (answer3)

    elif choice == "÷":
        answer4 = y*x/number1/number2
        print (answer4)

    else:
        print("ERROR")







variable2=(input("Please enter your Variable"))
constant1=(input("Please enter your Constant"))

variable(variable2,constant1)
