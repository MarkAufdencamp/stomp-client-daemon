from stomp_message_controller import StompMessageController
from stomp_message import StompMessage

class ApacheVirtualHostServiceController(StompMessageController):

	stomp_tasks = ["CreateApacheVirtualHost", "RemoveApacheVirtualHost", "EnableApacheVirtualHost", "DisableApacheVirtualHost", "CreateApacheVirtualHostProxy", "RemoveApacheVirtualHostProxy"]

	def run(self):
		print( "ApacheVirtualHostController" )

	def create_apache_virtual_host(self, stomp_message):
		print("CreateApacheVirtualHost - apache_virtual_host_service_controller.create_apache_virtual_host()")
		stomp_message.print_message()

	def remove_apache_virtual_host(self, stomp_message):
		print("RemoveApacheVirtualHost - apache_virtual_host_service_controller.remove_apache_virtual_host()")
		stomp_message.print_message()

	def enable_apache_virtual_host(self, stomp_message):
		print("EnableApacheVirtualHost - apache_virtual_host_service_controller.enable_apache_virtual_host()")
		stomp_message.print_message()

	def disable_apache_virtual_host(self, stomp_message):
		print("DisableApacheVirtualHost - apache_virtual_host_service_controller.disable_apache_virtual_host()")
		stomp_message.print_message()

	def create_apache_virtual_host_proxy(self, stomp_message):
		print("CreateApacheVirtualHostProxy - apache_virtual_host_service_controller.create_apache_virtual_host_proxy()")
		stomp_message.print_message()

	def remove_apache_virtual_host_proxy(self, stomp_message):
		print("RemoveApacheVirtualHostProxy - apache_virtual_host_service_controller.remove_apache_virtual_host_proxy()")
		stomp_message.print_message()
