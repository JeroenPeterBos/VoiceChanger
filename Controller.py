import threading
from Utils import Logger

# Debug values
view = True
model = False

if view:
	from GUI.main import MyApp

if model:
	from Communication import Protocol



class MainController:

	def changeVolume(self, volume, left, right):
		self.protocol.setVolume(volume, left, right);


	def changeMute(self, mute, left, right):
		self.protocol.setMute(mute, left, right)


	def run(self):
		self.logger.info("run", "Start all threads and open up gui and connections")
		if view:
			self.gui.run();
		if model:
			self.threads.append(self.protocol.startThread())
		return


	def close(self):
		# close all connections and wait for threads to finish
		return


	def __init__(self):
		self.logger = Logger.Logger(self)
		self.logger.info("__init__", "Initialize all components.")
		self.threads = []
		if view:
			self.gui = MyApp(self);
		if model:
			self.protocol = Protocol.Handler(self);
		return


	def getSimpleName(self):
		return "MainController"


program = MainController();
program.run();
