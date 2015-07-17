from stomp_message_controller import StompMessageController
from stomp_message import StompMessage

class StompRegistrationController(StompMessageController):
	
	stomp_tasks = ["Register", "Unregister", "SendPeerList", "UserMessage"]
	
	def run(self):
		print("StompRegistration")


	def register(self, stomp_message):
		print("Register - stomp_registration_controller.register()")
		stomp_message.print_message()

	def unregister(self, stomp_message):
		print("Unregister - stomp_registration_controller.unregister()")
		stomp_message.print_message()

	def send_peer_list(self, stomp_message):
		print("SendPeerList - stomp_registration_controller.send_peer_list()")
		stomp_message.print_message()

	def user__message():
		print("UserMessage - stomp_registration_controller.user_message()")
		stomp_message.print_message()
	
