from GUI.main import MyApp
from Communication.ComController import ComController

class MainController:

	def setVolume(self, val):
		self.com.setVolume(val);
	

	def run(self):
		self.gui.run();
		self.com.reset();
		return;


	def __init__(self):
		self.gui = MyApp(self);
		self.com = ComController(self);
		return;


program = MainController();
program.run();