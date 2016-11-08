import spidev
import time



	while True:
		spi = spidev.SpiDev()
		spi.mode = 0b00
		spi.max_speed_hz = 800000
		spi.open(0, 1)
		output = [0xBA]
		resp=spi.xfer2(output)
		print "new call"
		for d in resp:
			print "received byte: %d" % d
		spi.close()
	#end while
#end try
