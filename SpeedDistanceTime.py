#A simple Program that calculates the Speed, Distance and Time!
 
print("This is a simple Program that calculates the Speed, Distance and Time!")
triangle=input("Please choose a number to find out: 1. Speed 2. Distance 3. Time")
 
if triangle == "1":
    print("We will find the Speed")
    distance1=(int(input("Please enter the distance in Metres")))
    time1=(int(input("Please enter the time in seconds")))
    print("The speed will be in m/s")
    answer1 = distance1/time1
    print (answer1)
 
elif triangle == "2":
    print("We will find the Distance")
    speed2=(int(input("Please enter the the Speed in m/s")))
    time2=(int(input("Please enter the time in Seconds")))
    print("The distance will be in Metres")
    answer2 = speed2*time2
    print (answer2)
 
elif triangle == "3":
    print("We will find the Time")
    speed3=(int(input("Please enter the the Speed in m/s")))
    distance3=(int(input("Please enter the distance in Metres")))
    print("The time will be in Seconds")
    answer3 = distance3/speed3
    print (answer3)
 
else:
    print("ERROR")
 
print("Thanks for using this program")
end=input("End Of Program.....")
