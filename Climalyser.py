from time import sleep
from datetime import datetime


def climalyser():
    print("REMEMBER: 1 = lowest 5 = highest ")
    eletric=(int(input("How much does your Consumer Eletronics use effect the Enviroment?")))
    sleep(1)
    heat=(int(input("How does your home heating e.g Coal, Turf, Briquettes, Gas use effect the Enviroment?")))
    sleep(1)
    water=(int(input("How much Water would you use on a daily basis for tasks, 1 being the lowest and 5 the highest?")))
    sleep(1)
    ecology=(int(input("How much has Ecology/Biodiversity/Zoology/Local Habitats/Native Animals/Native Plants been affected by Pollution in your area")))
    sleep(1)
    transport=(int(input("How does your vehicular transport and/or daily,weekly,monthly commuting/travelling affect your local enviroment")))
    sleep(1)
    subtotal = eletric+heat+water+ecology+transport
    total = subtotal/25
    result = total*100
    result = str(result)
  
    if result >= "60":
        print("GOOD Quality")

    elif result <= "59":
        print("POOR Quality")

    else:
        print("ERROR")

    save=["Climate Change in your Life:"]
    save.append(result)
    print (save)

    target1 = open('yourlocalclimate.txt', 'w')

    target1.write(result)

    target1.close()

    print(result)
    sleep(20)
    

print("Welcome to 'Climalyser' the Local Climate Change Prediction Software")
sleep(2)
print("This software has been developed by Daniel O'Brien from Meteodeep")
sleep(2)
print("'Climalyser' is simply 'smart' survey software!! To operate you simply enter a number in, between 1 and 5 on how much a certain activity or parameter in YOUR local area/enviroment is affecting climate change locally (e.g Coastline Pollution/Industury Pollution) YOU then 'grade' this variable from 1 to 5 as mentioned earlier with 1 having least effect on the climate and 5 having most effect, this is all up to YOUR take on the climate around YOU")
sleep(2)
print("We will be regularly updating the software with bug fixes and updates/improvements")
sleep(2)
print("ENJOY!! and be sure to contact us for feedback!")

menu=input("Where would you like to go from here, 'Climalyser' or 'Website'")

if menu == "Climalyser":
    climalyser()
    
elif choice1 == "Website":
    print("www.tinyurl.com/meteodeep")

else:
    print("ERROR")


print("Thank You for using this Software, find the text file 'yourlocalclimate.txt' on your computer and this contains your RESULT out of 100 percent!!")
sleep(1)
print("Please Remember to fill in our 'World Climate' Survey on our website from the number (percentage) on the text file created (your result)")
sleep(2)
print("SHUTTING DOWN NOW!!")
