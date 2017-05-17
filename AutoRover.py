while True:
    import RPi.GPIO as GPIO #GPIO Libraries
    from time import sleep #Sleep Function

    GPIO.setmode(GPIO.BCM) #Setting Up

    GPIO.setup(23, GPIO.OUT)#Right Motor Forwards
    GPIO.setup(24, GPIO.OUT)# Backwards
    GPIO.setup(17, GPIO.OUT)#Left Motor Backwards
    GPIO.setup(27, GPIO.OUT)# Forwards


    print("Welcome to the AutoRobot!!!")
    sleep(2)
    control=input("G")

    if control=="G": #Moving Forward for 10 seconds to object
        GPIO.output(17, GPIO.HIGH)#On
        GPIO.output(24, GPIO.HIGH)
        sleep(10)#Wait 10 seconds
        GPIO.output(17, GPIO.LOW)#Off
        GPIO.output(24, GPIO.LOW)
    #Turning left for 5 seconds towards object    
        GPIO.output(24, GPIO.HIGH) #On
        sleep(5)                          
        GPIO.output(24, GPIO.LOW) #Off
        
        GPIO.output(17, GPIO.HIGH)#On
        GPIO.output(24, GPIO.HIGH)
        sleep(5)#Move forward 5 seconds parallel to object
        GPIO.output(17, GPIO.LOW)#Off
        GPIO.output(24, GPIO.LOW)
        
        GPIO.output(24, GPIO.HIGH) #On
        sleep(5)     #Turns left for 5 seconds away from object!                     
        GPIO.output(24, GPIO.LOW) #Off
        
        GPIO.output(17, GPIO.HIGH)#On
        GPIO.output(24, GPIO.HIGH)
        sleep(10)#Moves 10 seconds forward back to start/finish
        GPIO.output(17, GPIO.LOW)#Off
        GPIO.output(24, GPIO.LOW)
        
    else:
        print("ERROR")

    GPIO.cleanup()
