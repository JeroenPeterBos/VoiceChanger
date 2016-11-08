import Messages.Command

class Parser():

	def __init__(self, Protocol):
		self.currentCommand = None
		self.output = Protocol.spi.readQueue


	def parseBytes(self, parseBytes, result=False):
		if len(parseBytes) < 1:
			return result
		firstByte = parseBytes.pop(0)
		if self.currentCommand is None:
			if firstByte == 0x00:
				return parseBytes(self, parseBytes)
			else
				# self.currentCommand = ...  #create command from id
				return parseBytes(self, parseBytes, True)
		else:
			return parseBytes(self, parseBytes, moreToParse(self, firstByte))



	def moreToParse(self, byte):
		succes = self.currentCommand.addByte(byte)
		if self.currentCommand.isFilled():
			self.output.put(self.currentCommand)
			self.currentCommand = None
		return succes