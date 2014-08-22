import time
import pi2go

pi2go.init()

fast=50
slow=30

while True:
        dist = pi2go.getDistance()
        print "Distance: ", dist
        time.sleep(1)
pi2go.cleanup()
