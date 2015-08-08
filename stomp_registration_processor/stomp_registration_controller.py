import json
from stomp_message_controller import StompMessageController

class StompRegistrationController(StompMessageController):
	
	stomp_tasks = ["Register", "Unregister", "SendPeerList", "UserMessage", "MissingMethod"]
	
	def __init__(self):
		StompMessageController.__init__
		#print("StompRegistrationController.__init__()")
		self.registeredPeers = {}
	
	def run(self):
		print("StompRegistration.run()")

	def register(self, stomp_message):
		print("Register - stomp_registration_controller.register()")
		stomp_message.print_message()

		clientId = stomp_message.parsed_body['clientId']
		clientDesc = stomp_message.parsed_body['clientDesc']
		print("Registering Client Id - {0} - {1}".format(clientId, clientDesc))

		if (clientId not in self.registeredPeers):
			self.registeredPeers[clientId] = clientDesc
			self.broadcast_peer_list()

	def unregister(self, stomp_message):
		print("Unregister - stomp_registration_controller.unregister()")
		stomp_message.print_message()

		clientId = stomp_message.parsed_body['clientId']
		print("Unregistering Client Id - ", clientId)

		if (clientId in self.registeredPeers):
			del self.registeredPeers[clientId]
			self.broadcast_peer_list()

	def broadcast_peer_list(self):
		print("StompRegistrationController.broadcast_peer_list()")
		messageDict = {}
		messageDict["task"] = "PeerList"
		messageDict["registeredPeers"] = self.registeredPeers
		
		for clientId in self.registeredPeers:
			messageDict["clientId"] = clientId
			print(clientId, messageDict)
			self.send_message(clientId, messageDict)
	
	def send_peer_list(self, stomp_message):
		print("SendPeerList - stomp_registration_controller.send_peer_list()")
		stomp_message.print_message()

		clientId = stomp_message.parsed_body['clientId']
		#print("Registered Client Ids - ", self.registeredClients)
		#print("will be sent to {0}".format(clientId))
		messageDict = {}
		messageDict["task"] = "PeerList"
		messageDict["clientId"] = clientId
		messageDict["registeredPeers"] = self.registeredPeers
		#print(messageDict)
		self.send_message(clientId, messageDict)

	def user_message(self, stomp_message):
		print("UserMessage - stomp_registration_controller.user_message()")
		stomp_message.print_message()
	
	def send_message(self, clientId, messageDict):
		#print("StompRegistrationController() send_message")
		jsonMsg = json.dumps(messageDict)	
		messageQueue = "/queue/" + clientId
		#print(messageQueue)
		#print("Queue - {0}, Clients - {1}".format(messageQueue, self.registeredClients) )
		self.stompMessageBroker.sendMessage(jsonMsg, messageQueue)
