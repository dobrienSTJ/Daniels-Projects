while True:
    import RPi.GPIO as GPIO   #lets you use GPIO
    from time import sleep    #lets you use sleep(2) as a timer for the lights

    GPIO.setmode(GPIO.BCM)    #tells the program what labeling system to use

    GPIO.setup(23, GPIO.OUT)  #tells the pi exactly what number pin you'll be using
    GPIO.setup(24, GPIO.OUT)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)

    print("Welcome to the Awesome Robot!!!")
    sleep(1)

    control=input("Press 1 to move Forward or 2 to move Backwards or 3 to turn Right or 4 to turn Left")

    
    if control=="1":
        GPIO.output(23, GPIO.HIGH)#tells the pi to turn on this pin
        GPIO.output(24, GPIO.HIGH)
        sleep(10)               #Waits 10 seconds
        GPIO.output(23, GPIO.LOW)#tells the pi to turn off this pin
        GPIO.output(24, GPIO.LOW)

    elif control=="2":
        GPIO.output(17, GPIO.HIGH)#tells the pi to turn on this pin
        GPIO.output(27, GPIO.HIGH)
        sleep(10)               #Waits 10 seconds
        GPIO.output(17, GPIO.LOW)#tells the pi to turn off this pin
        GPIO.output(27, GPIO.LOW)

    elif control=="3":
        GPIO.output(23, GPIO.HIGH)#tells the pi to turn on this pin
        sleep(5)               #Waits 10 seconds
        GPIO.output(23, GPIO.LOW)#tells the pi to turn off this pin

    elif control=="4":
        #tells the pi to turn on this pin
        GPIO.output(24, GPIO.HIGH)
        sleep(5)               #Waits 10 seconds
        #tells the pi to turn off this pin
        GPIO.output(24, GPIO.LOW)
        
        

    else:
        print("ERROR")

    #the cleanup

    GPIO.cleanup()             #shuts down all GPIO stuff
