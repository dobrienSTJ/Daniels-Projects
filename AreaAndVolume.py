choice1=input("Please enter what you would like to use: 1. Area 2. Volume 3. Area of Cuboid")

if choice1 == "1":
    lenght1=(int(input("Please enter the Length")))
    width1=(int(input("Please enter the Width")))
    answer1 = lenght1*width1
    print (answer1)

elif choice1 == "2":
    lenght2=(int(input("Please enter the Length")))
    width2=(int(input("Please enter the Width")))
    depth2=(int(input("Please enter the Depth")))
    answer2 = lenght2*width2*depth2
    print (answer2)

elif choice1 == "3":
    lenght3=(int(input("Please enter the Length")))
    width3=(int(input("Please enter the Width")))
    height3=(int(input("Please enter the Height")))
    one = lenght3*width3*2
    two = lenght3*height3*2
    three = width3*height3*2
    answer3 = one+two+three
    print (answer3)
