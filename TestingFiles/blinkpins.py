import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM);

chan_list = [2,3,4,14,15,18,17,27,22,23,24,10,9,25,8,11,7];

for chan in chan_list:
	gpio.setup(chan, gpio.OUT);

for chan in chan_list:
	print "currently checking pin %d" % chan
	#print "value is %d" % gpio.input(chan)
	gpio.output(chan, 1)
	time.sleep(2)
	gpio.output(chan, 0)

gpio.cleanup()

