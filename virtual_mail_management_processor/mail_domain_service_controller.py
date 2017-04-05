from stomp_message_controller import StompMessageController
from stomp_message import StompMessage

class MailDomainServiceController(StompMessageController):

	stomp_tasks = ["CreateVirtualMailbox", "RemoveVirtualMailbox", "EnableVirtualMailbox", "DisableVirtualMailbox", "SetVirtualMailboxPasswd",  "CreateVirtualMailAlias", "RemoveVirtualMailAlias", "CreateRelayRecipient", "RemoveRelayRecipient"]

	def run(self):
		print( "VirtualMailboxController" )

	def create_virtual_mailbox(self, stomp_message):
		print("CreateVirtualMailbox - mail_domain_service_controller.create_virtual_mailbox()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessage = stomp_message.parsed_body
		acknowledgementQueue = acknowledgementMessage["service"]
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementQueue, acknowledgementMessage)
		else:
			self.acknowledge_failure(acknowledgementQueue, acknowledgementMessage)

	def remove_virtual_mailbox(self, stomp_message):
		print("RemoveVirtualMailbox - mail_domain_service_controller.remove_virtual_mailbox()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessage = stomp_message.parsed_body
		acknowledgementQueue = acknowledgementMessage["service"]
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementQueue, acknowledgementMessage)
		else:
			self.acknowledge_failure(acknowledgementQueue, acknowledgementMessage)

		successfulProvisioning = True
		
		acknowledgementMessage = stomp_message.parsed_body
		acknowledgementQueue = acknowledgementMessage["service"]
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementQueue, acknowledgementMessage)
		else:
			self.acknowledge_failure(acknowledgementQueue, acknowledgementMessage)

	def enable_virtual_mailbox(self, stomp_message):
		print("EnableVirtualMailbox - mail_domain_service_controller.enable_virtual_mailbox()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessage = stomp_message.parsed_body
		acknowledgementQueue = acknowledgementMessage["service"]
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementQueue, acknowledgementMessage)
		else:
			self.acknowledge_failure(acknowledgementQueue, acknowledgementMessage)

	def disable_virtual_mailbox(self, stomp_message):
		print("DisableVirtualMailbox - mail_domain_service_controller.disable_virtual_mailbox()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessage = stomp_message.parsed_body
		acknowledgementQueue = acknowledgementMessage["service"]
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementQueue, acknowledgementMessage)
		else:
			self.acknowledge_failure(acknowledgementQueue, acknowledgementMessage)

	def set_virtual_mailbox_passwd(self, stomp_message):
		print("SetVirtualMailboxPasswd - mail_domain_service_controller.set_virtual_mailbox_passwd()")
		stomp_message.print_message()

	def create_virtual_mail_alias(self, stomp_message):
		print("CreateVirtualMailAlias - mail_domain_service_controller.create_virtual_mail_alias()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessage = stomp_message.parsed_body
		acknowledgementQueue = acknowledgementMessage["service"]
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementQueue, acknowledgementMessage)
		else:
			self.acknowledge_failure(acknowledgementQueue, acknowledgementMessage)

	def remove_virtual_mail_alias(self, stomp_message):
		print("RemoveVirtualMailAlias - mail_domain_service_controller.remove_virtual_mail_alias()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessage = stomp_message.parsed_body
		acknowledgementQueue = acknowledgementMessage["service"]
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementQueue, acknowledgementMessage)
		else:
			self.acknowledge_failure(acknowledgementQueue, acknowledgementMessage)

	def create_relay_recipient(self, stomp_message):
		print("CreateRelayRecipient - mail_domain_service_controller.create_relay_recipient()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessage = stomp_message.parsed_body
		acknowledgementQueue = acknowledgementMessage["service"]
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementQueue, acknowledgementMessage)
		else:
			self.acknowledge_failure(acknowledgementQueue, acknowledgementMessage)

	def remove_relay_recipient(self, stomp_message):
		print("RemoveRelayRecipient - mail_domain_service_controller.remove_relay_recipient()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessage = stomp_message.parsed_body
		acknowledgementQueue = acknowledgementMessage["service"]
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementQueue, acknowledgementMessage)
		else:
			self.acknowledge_failure(acknowledgementQueue, acknowledgementMessage)

	def acknowledge_success(self, queue, message):
		print("== Acknowledge Message Success ==")
		self.send_message(queue, message)
	
	def acknowledge_failure(self, queue, message):
		print("== Acknowledge Message Failure ==")
		self.send_message(queue, message)
