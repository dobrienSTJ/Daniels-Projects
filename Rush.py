 0 9 * * 1 /pi/desktop/rushtourguide.py #Runs the Rush Tour Guide Program for Tourists at 9am every Monday 
  from time import sleep
  while True:
  
  print("Hello and Welcome to the Rush Tour Guide")
  sleep(2)
  print("You can search for the best attractions in the lovely seaside village of Rush Co. Dublin")
  sleep(2)
  print("For more Tourist Info: https://www.tripadvisor.ie/Tourism-g1389138-Rush_County_Dublin-Vacations.html")
  tourist=input("Type: 1.Attractions 2.Restraunts 3.Amenities 4.Accomadation")#Could also add Transport............
  tourist = tourist.upper()
  
  #Choosing the Topic you would like to learn about...........
  
  if tourist == "1":
    print("South Beach, North Beach, Drumnagh Martello Tower, Rush Harbour, Kenure House and Demense, St. Maurs Catholic Church")
    print("The beach is the best place to relax and chill in Rush and you have two other............")
    print("Towards the North of the Town you will find Kenure House..............")
    print("In the centre of the town as you drive in you see the Church...............")
    
  elif tourist == "2":
    print("Options for Good Food in Rush are plentiful and listed below:")
    print("Traditional:......")
    print("Cafe:.............")
    print("Chinese:........")
    print("Indian:...")
    print("Thai:......")
    
  elif tourist == "3":
    print("There are two top amenities in Rush!!")
    print("Every week the Rush Junior Parkrun takes place in Kenure Park on a Sunday......")
    print("The Millbank Theathre has many different performances throughout the year....")
    
  elif tourist == "4":
    print("SAndy Hills on the Sandy Road has the best B and B Accomadation........")
    
  else:
    print("Sorry, We haven't added " + tourist + " yet!")
    
  print("Thanks for using this program!!")
  sleep(2)
  print("Hope you enjoy your stay in Rush!!")
  
  #Output
  #An interactive menu system on info on Rush..........
