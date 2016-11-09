import spidev
import time

spi = spidev.SpiDev()
spi.mode = 0b00

spi.open(0, 1)

try:
	while True:
		output = [0xBA]
		resp=spi.xfer2(output)
		print("new call")
		print("received bytes: ")
		print(",".join(str(e) for e in resp))
		time.sleep(0.1)
	#end while
except KeyboardInterrupt:
	spi.close()
#end try
