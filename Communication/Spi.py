import Queue
import spidev
import time
import VoiceChanger.Utils.Logger

logging = True

class Spi:
	
	def getSimpleName(self):
		return "Spi"


	def __init__(self):
		self.logger = Logger.Logger(self, logging)
		self.writeQueue = Queue.Queue()
		self.readQueue = Queue.Queue()
		self.spi = spidev.SpiDev()
		self.spi.open(0, 1)


	def handleInOut(self):
		if not self.writeQueue.empty():
			return self.writeBytes(self, self.writeQueue.get().getBytes())
		else:
			return writeEmpty()


	def writeBytes(self, wBytes):
		self.logger.verbose("writeBytes", "Wrote the bytes [%s]" % ",".join(format(e, "02X") for e in wBytes))
		rbytes = []
		self.logger.verbose("writeBytes", "Read the bytes [ %s]" % ", ".join(format(e, "02X") for e in rBytes))
		#return response
		return


	def writeEmpty(self):
		self.logger.verbose("writeEmpty", "Wrote an empty byte to enable MISO transfer")
		rByte = 0x00
		self.logger.verbose("WriteEmpty", "Read a byte with the value of %d" % format(rByte, "02X"))
		return rByte


	def flush(self):
		command = self.writeQueue.get()
		return self.spi.xfer2(command.getBytes())


	def send(self, command):
		self.logger.info("send", "Added a command to the writeQueue")
		self.writeQueue.put(command)



	def read(self):
		self.logger.info("read", "Received a command from the readQueue")
		return self.readQueue.get();