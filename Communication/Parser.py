import Messages.Command

class Parser():

	def __init__(self, Protocol):
		self.currentCommand = None
		self.output = Protocol.spi.readQueue


	def parseBytes(self, parserBytes, result=False):
		if len(parserBytes) < 1:
			return result
		firstByte = parserBytes.pop(0)
		if self.currentCommand is None:
			if firstByte == 0x00:
				return self.parseBytes(parserBytes)
			else:
				# self.currentCommand = ...  #create command from id
				return self.parseBytes(parserBytes, True)
		else:
			return self.parseBytes(parserBytes, moreToParse(self, firstByte))



	def moreToParse(self, byte):
		succes = self.currentCommand.addByte(byte)
		if self.currentCommand.isFilled():
			self.output.put(self.currentCommand)
			self.currentCommand = None
		return succes
