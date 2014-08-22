import pi2go as p2
from time import sleep


p2.init()
a = p2.getDistance()
b = p2.irAll()
while True:
	if p2.getSwitch() == True:
		while a > 30 and b != True:
			p2.forward(75)
			p2.LsetLED(1,1)
			sleep(0.5)
			p2.LsetLED(1,0)
			a = p2.getDistance()
			b = p2.irAll()
		else:
			p2.spinRight(75)
			p2.LsetLED(1,1)
			sleep(0.7)
			p2.LsetLED(1,0)
			a = p2.getDistance()
			b = p2.irAll()

