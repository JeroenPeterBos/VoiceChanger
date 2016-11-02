from GUI.main import MyApp

class MainController:
	

	def run(self):
		self.gui.run();
		return;
	

	def printTest(self, message):
		print("test print: " + message);

	def __init__(self):
		self.gui = MyApp(self);
		return;

program = MainController();
program.run();