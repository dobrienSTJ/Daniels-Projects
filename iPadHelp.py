#A program on iPad Help!!
09**1/pi/desktop/ipadhelp.py #Plays this program every Monday at 9am
while True:  #While Loop
from time import sleep #pauses
from date import time  #Time/Date

    def mainprogram():  #The main program in a function
        print("Welcome to the iPad help Automated program")
        sleep(2)
        print("You can get help for 4 issues on this program:")
        sleep(2)
        issue=input("Type 'storage' for low storage problems, Type 'wifi' for Wi-Fi issues, Type 'edco' for Edco book problems, Type 'google for Google Account problems and Type 'slow' for a slow/laggy iPad")
        issue = issue.upper()

        if issue == "STORAGE":     #If statement for getting info on Problems
            storage()

        elif issue == "WIFI":
            wifi()

        elif issue == "EDCO":
            edco()

        elif issue == "GOOGLE":
            google()

        elif issue == "SLOW":
            slow()

        else:
            print("We don't have " + issue + " on our database yet")



        print("Thanks for using this program")  #Goodbye!
        sleep(2)
        print("Hopefully your issue was solved!")
        sleep(2)
        print("If not, email or visit Mr. Murray")


#All the different functions with Info on Problems!!

    def storage():
        print("A 16gb iPad is really only 11gb after iOS is Installed, delete some unessecary Games,Photos or Apps to free up Space")

    def wifi():
        print("Visit Mr. Murray at the ICT Office to ask for the School Wi-Fi password")

    def edco():
        print("Login to Edco books using your email login. This looks like this: [Year you started in St.Joseph's][First letter of first name][Second name]@stjosephsrush.ie Example: 16jsmith@stjosaephsrush.ie")
        print("This will be in the following format: [First four letters of first name, the first letter in upper case] [The at symbol "@"][The first three letters of your ipad screen unlock code] Example: John@123")
    
    def google():
        print("Login to your school Google account usin g just .com instaed of .ie")
    
    def slow():
        print("The problem is usually with Storage......")
        storage()
