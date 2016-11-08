import Spi
import Messages
import VoiceChanger.Utils.Logger
import Parser
import threading

logging = True


class Handler:

	def getSimpleName(self):
		return "ProtocolHandler"

	def __init__(self, controller):
		self.logger = Logger.Logger(self, logging)
		self.controller = controller;
		self.spi = Spi.Spi();
		self.parser = Parser(self)
		self.reset();


	# clears all the gpio settings and sets them to our desired defaults
	def reset(self):
		return


	# processes all the set values and updates the pins accordingly
	def update(self):
		self.spi.send(Messages.Volume(self.volume))

	
	def close(self):
		self.running = False


	def loop(self):
		self.running = True
		while self.running:
			self.cycle()


	def cycle(self):
		result = self.spi.handleInOut()
		self.parser.parseBytes(result)


	def startThread(self):
		thread = threading.Thread(target=self.loop())
		thread.start()
		return thread


	# Settings messages
	def setVolume(self, val, left, right):
		self.spi.send(Messages.Volume(val, left, right));