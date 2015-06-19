from stomp_message_controller import StompMessageController
from stomp_message_controller import StompMessage

class VirtualHostAccountController(StompMessageController):

	stomp_tasks = ["CreateVirtualHostAccount", "DeleteVirtualHostAccount", "EnableVirtualHostAcount", "DisableVirtualHostAccount"]

	def run(self):
		print( "VirtualHostAccountController" )

	def create_virtual_host_account(self):
		print("CreateVirtualHostAccount")

	def enable_virtual_host_account(self):
		print("EnableVirtualHostAccount")

	def disable_virtual_host_account(self):
		print("DisableVirtualHostAccount")

	def delete_virtual_host_account(self):
		print("DeleteVirtualHostAccount")
