from time import sleep
from datetime import datetime

def loginfunction_password():
    login_password=input("Please enter your account password")

    if login_password != "codingisthebest":
        print("Password is incorrect")
        sleep(2)
        loginfunction_password()

    elif login_password == "codingisthebest":
        print("Password is correct")
        sleep(2)
        print("Login Complete")
        sleep(2)
        print("Welcome, Coding Master!")
        sleep(2)
        onlineshoppingconsole()

def loginfunction_email():
    login_email=input("Please enter your email")

    if login_email != "codingexamples@stjosephsrush.ie":
        print("Email Incorrect")
        sleep(2)
        loginfunction_email()
        
    elif login_email == "codingexamples@stjosephsrush.ie":
        print("Email Correct")
        sleep(2)
        loginfunction_password()

def onlineshoppingconsole():
    subtotal = (8)
    sleep(2)
    print("Your current sub-total is €8")
    print (subtotal)
    sleep(2)
    cart = ["Postage and Packaging"]
    sleep(2)
    print("You currently have a postage and packaging charge of €8")
    sleep(2)
    print (cart)
    sleep(2)
    print("You will be able to purchase a wide range of the newest GoPro cameras on this page!")

    
    print("What would you like to purchase in the store, we have the following in stock today")
    buy_choice=input("Hero 5 Black (€430), Hero 5 Session (€330), Hero 4 Session (€230), Karma Drone (€870) and also the Hero 5 Black + Karma Drone Combo Deal (€1100), for this purchase please enter: Hero 5 Black Karma Drone")

    if buy_choice== "Hero 5 Black":
        cart.append("Hero 5 Black")
        subtotal = subtotal+430
        print("You have added Hero 5 Black to your cart")
            

    elif buy_choice== "Hero 5 Sesssion":
        cart.append("Hero 5 Session")
        subtotal = subtotal+330
        print("You have added Hero 5 Sesssion to your cart")
            

    elif buy_choice== "Hero 4 Session":
        cart.append("Hero 4 Session")
        subtotal = subtotal+230
        print("You have added Hero 4 Session to your cart")
            

    elif buy_choice== "Karma Drone":
        cart.append("Karma Drone")
        subtotal = subtotal+870
        print("You have added Karma Drone to your cart")
           

    elif buy_choice== "Hero 5 Black Karma Drone":
        cart.append("Karma Drone + Hero 5 Black Combo")
        subtotal = subtotal+1100
        print("You have added this product to your cart")
           

    else:
        print("We do not currently sell "+ buy_choice +", sorry for any inconvience caused")
            


    print("We will now continue to the purchasing your item, if your product was over €300 you can avail of FREE DELIVERY and POSTAGE AND PACKAGING")

    if subtotal  >= 300:
        print("You can avail of FREE DELIVERY and P&P!")
        del cart[0]
        subtotal = subtotal-8

    elif subtotal <= 299:
        print("Sorry you could not avail of the offer")

    print("The following price is the subtotal for your purchase...")
    sleep(2)
    print("First we will add VAT")
    sleep(2)
    vat = subtotal/100*23
    subtotal = subtotal+vat
    print(subtotal)
    print("Here are your purchases....")
    sleep(2)
    for item in cart:
        print(item)

    for item in cart:
        if item == "Hero 5 Black" or item == "Hero 5 Session":
            print("These are new products that will be released on October the 2nd")
        elif item == "Karma Drone":
            print("This product will be released on October 23rd")
        else:
            print("This product will be shipped and delivered in the next 3-5 business days")
            
            

    print("The purchase page will open NOW")
    sleep(3)
    purchase_creditcard=input("Please enter your credit card number, confirm your purchase and confirm that you accept the terms and conditions e.g xxxxxxxx yes yes")

    #Credit Card Number: 12345678
    if purchase_creditcard != "12345678 yes yes":
          print("ERROR")
          sleep(2)
          print("You will return to the homepage NOW")
          onlineshoppingconsole()

    elif purchase_creditcard == "12345678 yes yes":
          print("Your Purchased Has Been Made!")
          sleep(2)
          print("Thank You for shopping with GoPro!")
          ending()

def ending():
    print("Thank You for shopping with GoPro today! (powered by Amazon)")
    sleep(2)
    print("Ww will send your receipt by email and any other GoPro deals in the Future!")

    end=input("Confirm Form Resubmission?")
   
timenow = datetime.now()
print (timenow)
sleep(2)
print("Welcome to the GoPro Store on Amazon")
sleep(2)
print("Please enter your login details to continue")
sleep(2)
#Email: codingexamples@stjosephsrush.ie
loginfunction_email()
#Password: codingisthebest
loginfunction_password()

#So this is the code hopefully everything worked out and your purchase was made sucsessfully!!!!
