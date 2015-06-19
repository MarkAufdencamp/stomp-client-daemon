from stomp_message_controller import StompMessageController
from stomp_message_controller import StompMessage

class ApacheVirtualHostController(StompMessageController):

	stomp_tasks = ["CreateApacheVirtualHost", "DeleteApacheVirtualHost", "EnableApacheVirtualHost", "DisableApacheVirtualHost"]

	def run(self):
		print( "ApacheVirtualHostController" )

	def create_apache_virtual_host(self):
		print("CreateApacheVirtualHost")

	def enable_apache_virtual_host(self):
		print("EnableApacheVirtualHost")

	def disable_apache_virtual_host(self):
		print("DisableApacheVirtualHost")

	def delete_apache_virtual_host(self):
		print("DeleteApacheVirtualHost")
