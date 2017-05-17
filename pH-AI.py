#This program can also be used as a CSI Investigator:-)!!!!!!
#The program starts with the scale at 50 (neutral)

scale =int(50) 

print("Your pH meter is broken!!, But DO NOT despair!!! Help is Here!!!")

#We then have a long list of inputs explaining the different indicators

taste=input("Please enter the taste of the liquid") 

if taste == "sour":
    scale = (scale+25)

elif taste == "normal" or taste == "sweet":
    scale = (scale+0)
       
else:
    print("This program has not registered this taste!")

cleaning=input("Is this sample used commonly in cleaning/washing or baking")

if cleaning == "yes":
    scale = (scale-60)

elif cleaning == "no":
    scale = (scale+0)

else:
    print("ERROR")


litmus=input("Please enter what colour litmus paper turns when added to the substance")

if litmus == "blue":
    scale = (scale-25)

elif litmus == "red":
    scale = (scale+25)

elif litmus == "stays the same":
    scale = (scale+0)

else:
    print("ERROR")


redcabbage=input("If you have used red cabbage indicator what colour has it turned?")

if redcabbage == "blue":
               scale = (scale-75)

elif redcabbage == "purple":
               scale = (scale+0)

elif redcabbage == "pink":
               scale = (scale+75)

else:
               print("ERROR")


rainfall=input("By any chance is the sample Rain Water????")

if rainfall == "yes":
               scale = (scale+0)

elif rainfall == "no":
               scale = (scale+0)

else:
               print("ERROR")

#The program will then print out the answer on the scale (instructions below)


print("If your scale is 100 or more most likely to be acid, around 0 most likely neutral, less than 0 most likely a base")
print (scale)
print("Thank you for using this program, improvemnts are always being made!!!!!!")
