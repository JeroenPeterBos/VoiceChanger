class ComController:

	def __init__(self, controller):
		self.controller = controller;
		reset();


	# clears all the gpio settings and sets them to our desired defaults
	def reset(self):
		self.volume = 7;


	# processes all the set values and updates the pins accordingly
	def update(self):


	def setVolume(self, val):
