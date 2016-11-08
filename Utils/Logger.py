verbose = 0
debug = 1
info = 2
warning = 3
error = 4

log_level = debug

class Logger():

	def __init__(self, logloc, logging=True):
		self.logloc = logloc
		self.logging = logging

	def debug(self, method, message):
		if self.logging and log_level <= debug:
			print("[{:<8}][{:>15}] - {:>10}(*):    {:<100}".format("DEBUG", self.logloc.getSimpleName(), method, message))


	def info(self, method, message):
		if self.logging and log_level <= info:
			print("[{:<8}][{:>15}] - {:>10}(*):    {:<100}".format("INFO", self.logloc.getSimpleName(), method, message))


	def warning(self, method, message):
		if self.logging and log_level <= warning:
			print("[{:<8}][{:>15}] - {:>10}(*):    {:<100}".format("WARNING", self.logloc.getSimpleName(), method, message))


	def error(self, method, message):
		if self.logging and log_level <= error:
			print("[{:<8}][{:>15}] - {:>10}(*):    {:<100}".format("ERROR", self.logloc.getSimpleName(), method, message))


	def verbose(self, method, message):
		if self.logging and log_level <= verbose:
			print("[{:<8}][{:>15}] - {:>10}(*):    {:<100}".format("VERBOSE", self.logloc.getSimpleName(), method, message))
