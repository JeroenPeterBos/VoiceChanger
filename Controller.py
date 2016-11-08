import threading

# Debug values
view = True
model = False

if view:
	from GUI.main import MyApp

if model:
	import Communication.Protocol



class MainController:

	def changeVolume(self, volume, left, right):
		self.protocol.setVolume(volume, left, right);


	def run(self):
		print "[MainController] - Start all threads and open up gui and connections"
		if view:
			self.gui.run();
		if model:
			self.threads.append(self.protocol.startThread())
		return
		

	def close(self):
		# close all connections and wait for threads to finish
		return


	def __init__(self):
		print "[MainController] - Initialize all components"
		self.threads = []
		if view:
			self.gui = MyApp(self);
		if model:
			self.protocol = Protocol.Handler(self);
		return;


program = MainController();
program.run();