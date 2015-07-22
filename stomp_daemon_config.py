import json
import socket

class StompDaemonConfig:
	
	def __init__(self, config_file, processors_file):
		print("StompDaemonConfig constructor")

		self.config_file_name = config_file
		self.processors_file_name = processors_file

		self.loadConfig()
		self.parseConfig()
		self.validateConfig()

		self.loadProcessors()
		self.validateProcessors()

	def loadConfig(self):
		print("StompDaemonConfig load")
		# Load the configuration file
		self.config = json.load(open('config.json'))

	def parseConfig(self):
		print("StompDaemonConfig parseConfig")
		self.msgSrvr = "localhost"
		self.msgSrvrPort = "61613"
		self.msgSrvrQueue = "/queue/stomp-message-processor-server.local"
		self.msgSrvrClientId = "stomp-message-processor-server.local"

		try:
			self.msgSrvr = self.config['msgSrvr']
		except KeyError:
			print("Error loading msgSrvr from config.json - Utilizing default - 'localhost'")
		try:
			self.msgSrvrPort = self.config['msgSrvrPort']
		except KeyError:
			print("Error loading msgSrvrPort from config.json - Utilizing default - '61613'")
		try:
			self.msgSrvrQueue =  self.config['msgSrvrQueue']
		except KeyError:
			print("Error loading msgSrvrQueue from config.json - Utilizing default - '/queue/stomp-message-server-processor.local'")
		try:
			self.msgSrvrClientId = self.config['msgSrvrClientId']
		except KeyError:
			print("Error loading msgSrvrClientId from config.json - Utilizing default - 'stomp-message-processor-server.local'")

	def validateConfig(self):
		print("StompDaemonConfig validateConfig")
		self.hostname = socket.gethostbyaddr(socket.gethostname())[0]
		self.ip_addresses = socket.gethostbyname_ex(socket.gethostname())[2]
	
	def loadProcessors(self):
		print("StompDaemonConfig loadProcessors")
		self.processors = json.load(open('processors.json'))
		
	def validateProcessors(self):
		print("StompDaemonConfig validateProcessors")
		


