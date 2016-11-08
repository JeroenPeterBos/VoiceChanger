class Command:

	def __init__(self, amountOfParamBytes=0, amountOfValueBytes=0):
		self.identifier = 0x00
		self.parameters = []
		self.values = []
		self.aopbytes = amountOfParamBytes
		self.aovbytes = amountOfValueBytes


	def getBytes(self):
		result = []
		result.append(self.identifier)
		result.extend(self.parameters)
		result.extend(self.values)
		return result


	def setAmountOfParamBytes(self, value):
		self.aopbytes = value


	def setAmountOfValueBytes(self, value):
		self.aovbytes = value


	def addByte(self, byte):
		if self.aopbytes < len(self.parameters):
			self.parameters.put(byte)
		elif self.aovbytes < len(self.values):
			self.values.put(byte)
		else:
			return False
		return True

	def isFilled(self):
		return ((aopbytes == len(self.parameters)) and (aovbytes == len(self.values)))


class Volume(Command):

	def __init__(self, volume=0b1111001, left=True, right=True):
		Command.__init__(self, 0, 2)
		self.identifier = 0x02
		self.volume = volume
		self.left = left
		self.right = right


	def setVolume(self, volume):
		self.volume = volume

	def fillBytes(self):
		self.parameters = []
		self.values = []
		address = 0b00000100
		if self.right:
			address = address | 0b10
			if self.left:
				address = address | 0b1
		self.values.append(address)
		self.values.append(self.volume)

	def getBytes(self):
		self.fillBytes()
		return Command.getBytes(self)


class Mute(Command):

	def __init__(self, mute=True, left=True, right=True):
		Command.__init__(self, 0, 0)
		self.identifier = 0x04


def parseNewCommand(identifier):
	return {
		0x02: Volume()
		0x04: Mute()
	}[identifier]



# Testing
#volumeCommand = parseNewCommand(0x02)
#bytesarray = volumeCommand.getBytes()

#for byte in bytesarray:
#	print "got byte %s" % bin(byte)
