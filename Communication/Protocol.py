import Spi
import Messages

class Handler:

	def __init__(self, controller):
		self.controller = controller;
		self.spi = Spi.Spi();
		self.reset();


	# clears all the gpio settings and sets them to our desired defaults
	def reset(self):
		return


	# processes all the set values and updates the pins accordingly
	def update(self):
		self.spi.send(Messages.Volume(self.volume))


	def setVolume(self, val, left, right):
		self.spi.send(Messages.Volume(val, left, right));


	def loop():
		return