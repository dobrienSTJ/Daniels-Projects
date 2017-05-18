while True:
	
	from sense_hat import SenseHat

	sense = SenseHat()
	sense.clear()

	pressure = sense.get_pressure()
	pressure = round(pressure, 1)
	print(pressure)

	temp = sense.get_temperature()
	temp = round(temp,1)
	print(temp)

	humidity = sense.get_humidity()
	humidity = round(humidity, 1)
	print(humidity)
