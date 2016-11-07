class Command:

	childs = []

	def __init__(self):
		self.identifier = 0x00
		self.parameters = []
		self.values = []


	def getBytes(self):
		result = []
		result.append(self.identifier)
		result.extend(self.parameters)
		result.extend(self.values)
		return result


class Volume(Command):
	def __init__(self, volume=0b1111001, left=True, right=True):
		Command.__init__(self)
		self.identifier = 0x02
		self.volume = volume
		self.left = left
		self.right = right


	def setVolume(self, volume):
		self.volume = volume


	def getBytes(self):
		address = 0b00000100
		if self.right:
			address = address | 0b10
			if self.left:
				address = address | 0b1
		self.values.append(address)
		self.values.append(self.volume)
		return Command.getBytes(self)

# register existing identification codes
Command.childs.append(Volume.identifier)


volumeCommand = Volume(0b1111001, False, True)
bytesarray = volumeCommand.getBytes()

for byte in bytesarray:
	print "got byte %s" % bin(byte)