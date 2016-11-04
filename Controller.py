from GUI.main import MyApp
import Communication.Protocol
import Communication.Spi
import threading

class MainController:

	def setVolume(self, val):
		self.protocol.setVolume(val);


	def run(self):
		print "[MainController] - Start all threads and open up gui and connections"
		# start the spithread that will handle output and input
		spithread = threading.Thread(target=self.spi.loop())
		self.threads.append(spithread)
		spithread.start()

		self.gui.run();
		self.protocol.reset();
		return;

	def close(self):
		# close all connections and wait for threads to finish

	def __init__(self):
		print "[MainController] - Initialize all components"
		self.threads = []
		self.spi = Spi.Spi()
		self.gui = MyApp(self);
		self.protocol = Protocol.Handler(self);
		return;


program = MainController();
program.run();