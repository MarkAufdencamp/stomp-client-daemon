from stomp_message_controller import StompMessageController
from stomp_message_controller import StompMessage

class PostfixVirtualHostController(StompMessageController):

	stomp_tasks = ["CreatePostfixVirtualHost", "DeletePostfixVirtualHost", "EnablePostfixVirtualHost", "DisablePostfixVirtualHost"]

	def run(self):
		print( "PostfixVirtualHostController" )

	def create_postfix_virtual_host(self):
		print("CreatePostfixVirtualHost")

	def enable_postfix_virtual_host(self):
		print("EnablePostfixVirtualHost")

	def disable_postfix_virtual_host(self):
		print("DisablePostfixVirtualHost")

	def delete_postfix_virtual_host(self):
		print("DeletePostfixVirtualHost")
