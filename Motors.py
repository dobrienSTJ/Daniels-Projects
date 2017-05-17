while True:
    import RPi.GPIO as GPIO #GPIO Libraries
    from time import sleep #Sleep Functions

    GPIO.setmode(GPIO.BCM) #Setting Up

    GPIO.setup(23, GPIO.OUT)#Right Motor Forwards
    GPIO.setup(24, GPIO.OUT)# Backwards
    GPIO.setup(17, GPIO.OUT)#Left Motor Backwards
    GPIO.setup(27, GPIO.OUT)# Forwards


    print("Welcome to the Awesome Robot!!!")
    sleep(2)
    control=input("Press 1 to move Forward or 2 to turn Right or 3 to turn Leftn and 4 to move Backwards!")

    if control=="1": #Moving Forward
        GPIO.output(17, GPIO.HIGH)#On
        GPIO.output(24, GPIO.HIGH)
        sleep(10)#Wait 10 seconds
        GPIO.output(17, GPIO.LOW)#Off
        GPIO.output(24, GPIO.LOW)
        
        
    elif control=="2":
        GPIO.output(17, GPIO.HIGH) #On
        sleep(5)                          
        GPIO.output(17, GPIO.LOW) #Off 
        

    elif control=="3": #Turning Left
        GPIO.output(24, GPIO.HIGH) #On
        sleep(5)
        GPIO.output(24, GPIO.LOW) #On	
	        
    elif control=="4":
        GPIO.output(27, GPIO.HIGH)#On
        GPIO.output(23, GPIO.HIGH)
        sleep(10)
        GPIO.output(27, GPIO.LOW)
        GPIO.output(23, GPIO.LOW)
        
    else:
        print("ERROR")

#INSERT ULTRA-SONIC CODE HERE# 

    GPIO.cleanup()
