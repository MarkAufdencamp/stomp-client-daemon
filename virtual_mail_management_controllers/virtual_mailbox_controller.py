from stomp_message_controller import StompMessageController
from stomp_message_controller import StompMessage

class VirtualMailboxController(StompMessageController):

	stomp_tasks = ["CreateVirtualMailbox", "DeleteVirtualMailbox", "EnableVirtualMailbox", "DisableVirtualMailbox"]

	def run(self):
		print( "VirtualMailboxController" )

	def create_virtual_mailbox(self):
		print("CreateVirtualMailbox")

	def enable_virtual_mailbox(self):
		print("EnableVirtualMailbox")

	def disable_virtual_mailbox(self):
		print("DisableVirtualMailbox")

	def delete_virtual_mailbox(self):
		print("DeleteVirtualMailbox")
