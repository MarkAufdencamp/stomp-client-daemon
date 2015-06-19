from stomp_message_controller import StompMessageController
from stomp_message_controller import StompMessage

class StompRegistrationController(StompMessageController):
	
	stomp_tasks = ["Register", "Unregister", "SendPeerList"]
	
	def run(self):
		print("StompRegistration")

	def register():
		print("Register")

	def unregister():
		print("Unregister")

	def send_client_peer_list():
		print("SendPeerList")
