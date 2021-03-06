from stomp_message_controller import StompMessageController
from stomp_message import StompMessage

class PostfixDovecotVirtualHostServiceController(StompMessageController):

	stomp_tasks = ["CreatePostfixDovecotVirtualHost", "RemovePostfixDovecotVirtualHost", "EnablePostfixDovecotVirtualHost", "DisablePostfixDovecotVirtualHost", "CreatePostfixDovecotVirtualHostRelay", "RemovePostfixDovecotVirtualHostRelay"]

	def run(self):
		print( "PostfixVirtualHostController" )

	def create_postfix_dovecot_virtual_host(self, stomp_message):
		print("CreatePostfixDovecotVirtualHost - postfix_dovecot_virtual_host_service_controller.create_postfix_dovecot_virtual_host()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessageDict = stomp_message.parsed_body
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementMessageDict)
		else:
			self.acknowledge_failure( acknowledgementMessageDict)

	def remove_postfix_dovecot_virtual_host(self, stomp_message):
		print("RemovePostfixDovecotVirtualHost - postfix_dovecot_virtual_host_service_controller.remove_postfix_dovecot_virtual_host()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessageDict = stomp_message.parsed_body
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementMessageDict)
		else:
			self.acknowledge_failure(acknowledgementMessageDict)

	def enable_postfix_dovecot_virtual_host(self, stomp_message):
		print("EnablePostfixDovecotVirtualHost - postfix_dovecot_virtual_host_service_controller.enable_postfix_dovecot_virtual_host()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessageDict = stomp_message.parsed_body

		if successfulProvisioning:
			self.acknowledge_success(acknowledgementMessageDict)
		else:
			self.acknowledge_failure(acknowledgementMessageDict)

	def disable_postfix_dovecot_virtual_host(self, stomp_message):
		print("DisablePostfixDovecotVirtualHost - postfix_dovecot_virtual_host_service_controller.disable_postfix_dovecot_virtual_host()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessageDict = stomp_message.parsed_body
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementMessageDict)
		else:
			self.acknowledge_failure(acknowledgementMessageDict)

	def create_postfix_dovecot_virtual_host_relay(self, stomp_message):
		print("CreatePostfixDovecotVirtualHostRelay - postfix_dovecot_virtual_host_service_controller.create_postfix_dovecot_virtual_host_relay()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessageDict = stomp_message.parsed_body
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementMessageDict)
		else:
			self.acknowledge_failure(acknowledgementMessageDict)

	def remove_postfix_dovecot_virtual_host_relay(self, stomp_message):
		print("RemovePostfixDovecotVirtualHostRelay - postfix_dovecot_virtual_host_service_controller.remove_postfix_dovecot_virtual_host_relay()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessageDict = stomp_message.parsed_body
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementMessageDict)
		else:
			self.acknowledge_failure(acknowledgementMessageDict)

	def acknowledge_success(self, acknowledgementMessageDict):
		print("== Acknowledge Message Success ==")
		acknowledgementQueue = acknowledgementMessageDict["service"]
		acknowledgementMessageDict["taskResult"] = "Success"
		self.send_message(acknowledgementQueue, acknowledgementMessageDict)
	
	def acknowledge_failure(self, acknowledgementMessageDict):
		print("== Acknowledge Message Failure ==")
		acknowledgementQueue = acknowledgementMessageDict["service"]
		acknowledgementMessageDict["taskResult"] = "Failure"
		self.send_message(acknowledgementQueue, acknowledgementMessageDict)
