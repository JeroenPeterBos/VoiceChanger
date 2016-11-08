import spidev
import time

output = [0xAB]

while True:
	spi = spidev.SpiDev()
	spi.open(0, 1)
	spi.mode = 0b00
	spi.max_speed_hz = 800000
	resp=spi.xfer2(output)
	spi.close()
	
	print "new call"
	for d in resp:
		print "received byte: 0x%s" % format(d, "02X")	
	time.sleep(0.3)
