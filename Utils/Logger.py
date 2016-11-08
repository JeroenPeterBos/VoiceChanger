class Logger():

	def __init__(self, logloc, logging=True):
		self.logloc = logloc
		self.logging = logging

	def debug(self, method, message):
		if logging:
			print("[{:<8}][{:>15}] - {:>15}(*):    {:<100}".format("DEBUG", self.logloc.getSimpleName(), method, message))


	def info(self, method, message):
		if logging:
			print("[{:<8}][{:>15}] - {:>15}(*):    {:<100}".format("INFO", self.logloc.getSimpleName(), method, message))


	def warning(self, method, message):
		if logging:
			print("[{:<8}][{:>15}] - {:>15}(*):    {:<100}".format("WARNING", self.logloc.getSimpleName(), method, message))


	def error(self, method, message):
		if logging:
			print("[{:<8}][{:>15}] - {:>15}(*):    {:<100}".format("ERROR", self.logloc.getSimpleName(), method, message))


	def verbose(self, method, message):
		if logging:
			print("[{:<8}][{:>15}] - {:>15}(*):    {:<100}".format("VERBOSE", self.logloc.getSimpleName(), method, message))