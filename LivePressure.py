from time import sleep
	
from sense_hat import SenseHat


sense = SenseHat()
sense.clear()

pressure = sense.get_pressure()
pressure = round(pressure, 1)
pressure = str(pressure)
	
target1 = open('/var/www/meteodeep/pressure.txt', 'w')
target1.write(pressure)
target1.close()

sleep(900)

target1.truncate()

# crontab
# */15 * * * * sudo /usr/bin/python3 /var/www/meteodeep/LivePressure.py
