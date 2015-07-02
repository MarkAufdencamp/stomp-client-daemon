from stomp_message_controller import StompMessageController
from stomp_message import StompMessage

class MailDomainServiceController(StompMessageController):

	stomp_tasks = ["CreateVirtualMailbox", "RemoveVirtualMailbox", "EnableVirtualMailbox", "DisableVirtualMailbox", "SetVirtualMailboxPasswd",  "CreateVirtualMailAlias", "RemoveVirtualMailAlias", "CreateRelayRecipient", "RemoveRelayRecipient"]

	def run(self):
		print( "VirtualMailboxController" )

	def create_virtual_mailbox(self, stomp_message):
		print("CreateVirtualMailbox - mail_domain_service_controller.create_virtual_mailbox()")
		stomp_message.print_message()

	def remove_virtual_mailbox(self, stomp_message):
		print("RemoveVirtualMailbox - mail_domain_service_controller.remove_virtual_mailbox()")
		stomp_message.print_message()

	def enable_virtual_mailbox(self, stomp_message):
		print("EnableVirtualMailbox - mail_domain_service_controller.enable_virtual_mailbox()")
		stomp_message.print_message()

	def disable_virtual_mailbox(self, stomp_message):
		print("DisableVirtualMailbox - mail_domain_service_controller.disable_virtual_mailbox()")
		stomp_message.print_message()

	def set_virtual_mailbox_passwd(self, stomp_message):
		print("SetVirtualMailboxPasswd - mail_domain_service_controller.set_virtual_mailbox_passwd()")
		stomp_message.print_message()

	def create_virtual_mail_alias(self, stomp_message):
		print("CreateVirtualMailAlias - mail_domain_service_controller.create_virtual_mail_alias()")
		stomp_message.print_message()

	def remove_virtual_mail_alias(self, stomp_message):
		print("RemoveVirtualMailAlias - mail_domain_service_controller.remove_virtual_mail_alias()")
		stomp_message.print_message()

	def create_relay_recipient(self, stomp_message):
		print("CreateRelayRecipient - mail_domain_service_controller.create_relay_recipient()")
		stomp_message.print_message()

	def remove_relay_recipient(self, stomp_message):
		print("RemoveRelayRecipient - mail_domain_service_controller.remove_relay_recipient()")
		stomp_message.print_message()

