import Spi
import Messages
from Utils import Logger
import Parser
import threading
import time

logging = True


class Handler:

	def getSimpleName(self):
		return "ProtocolHandler"

	def __init__(self, controller):
		self.logger = Logger.Logger(self, logging)
		self.controller = controller;
		self.spi = Spi.Spi();
		self.parser = Parser.Parser(self)
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
			time.sleep(0.1)


	def cycle(self):
		result = self.spi.handleInOut()
		if self.parser.parseBytes(result):
			return self.cycle()


	def startThread(self):
		thread = threading.Thread(target=self.loop())
		thread.start()
		return thread


	# Settings messages
	def setVolume(self, val, left, right):
		self.spi.send(Messages.Volume(val, left, right));


	def setMute(self, mute, left, right):
		self.spi.send(Messages.Mute(mute, left, right));