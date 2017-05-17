def usdconversion():
    usdmoney=(int(input("Please enter the amount of EURO you would like to convert to USD")))
    usdconverter = 0.89285714285
    usdmoney = usdconverter*usdmoney
    print(usdmoney)
        
#British Conversions
def gbpconversion():
    gbpmoney=(int(input("Please enter the amount of EURO you would like to convert to GBP")))
    gbpconverter = 1.11
    gbpmoney = gbpconverter*gbpmoney
    print(gbpmoney)
        

        


#Menu System
print("Welcome to the Currency Converter!")
currency_selection=input("What Currency would you like to convert to from EURO?, USD(US Dollars), GBP(British Pound Sterling)")
    
if currency_selection == "USD":
    print("Ok, US Dollars Converter......")
    usdconversion()

elif currency_selection == "GBP":
    print("Ok, British Pound Sterling Converter......")
    gbpconversion()

else:
    print("We don't have that Currency yet, search 'currency converter' on Google")
