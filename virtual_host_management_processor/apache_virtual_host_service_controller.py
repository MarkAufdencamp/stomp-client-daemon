from stomp_message_controller import StompMessageController
from stomp_message import StompMessage

class ApacheVirtualHostServiceController(StompMessageController):

	stomp_tasks = ["CreateApacheVirtualHost", "RemoveApacheVirtualHost", "EnableApacheVirtualHost", "DisableApacheVirtualHost", "CreateApacheVirtualHostProxy", "RemoveApacheVirtualHostProxy"]

	def run(self):
		print( "ApacheVirtualHostController" )

	def create_apache_virtual_host(self, stomp_message):
		print("CreateApacheVirtualHost - apache_virtual_host_service_controller.create_apache_virtual_host()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessage = stomp_message.parsed_body
		acknowledgementQueue = acknowledgementMessage["service"]
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementQueue, acknowledgementMessage)
		else:
			self.acknowledge_failure(acknowledgementQueue, acknowledgementMessage)

	def remove_apache_virtual_host(self, stomp_message):
		print("RemoveApacheVirtualHost - apache_virtual_host_service_controller.remove_apache_virtual_host()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessage = stomp_message.parsed_body
		acknowledgementQueue = acknowledgementMessage["service"]
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementQueue, acknowledgementMessage)
		else:
			self.acknowledge_failure(acknowledgementQueue, acknowledgementMessage)

	def enable_apache_virtual_host(self, stomp_message):
		print("EnableApacheVirtualHost - apache_virtual_host_service_controller.enable_apache_virtual_host()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessage = stomp_message.parsed_body
		acknowledgementQueue = acknowledgementMessage["service"]
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementQueue, acknowledgementMessage)
		else:
			self.acknowledge_failure(acknowledgementQueue, acknowledgementMessage)

	def disable_apache_virtual_host(self, stomp_message):
		print("DisableApacheVirtualHost - apache_virtual_host_service_controller.disable_apache_virtual_host()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessage = stomp_message.parsed_body
		acknowledgementQueue = acknowledgementMessage["service"]
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementQueue, acknowledgementMessage)
		else:
			self.acknowledge_failure(acknowledgementQueue, acknowledgementMessage)

	def create_apache_virtual_host_proxy(self, stomp_message):
		print("CreateApacheVirtualHostProxy - apache_virtual_host_service_controller.create_apache_virtual_host_proxy()")
		stomp_message.print_message()

	def remove_apache_virtual_host_proxy(self, stomp_message):
		print("RemoveApacheVirtualHostProxy - apache_virtual_host_service_controller.remove_apache_virtual_host_proxy()")
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
