from stomp_message_controller import StompMessageController
from stomp_message import StompMessage

class TomcatVirtualHostServiceController(StompMessageController):
	
	stomp_tasks = ["CreateTomcatVirtualHost", "RemoveTomcatVirtualHost", "EnableTomcatVirtualHost", "DisableTomcatVirtualHost"]
	
	def run(self):
		print("TomcatVirtualHostServiceController")

	def create_tomcat_virtual_host(self, stomp_message):
		print("CreateTomcatVirtualHost - tomcat_virtual_host_service_controller.create_tomcat_virtual_host()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessage = stomp_message.parsed_body
		acknowledgementQueue = acknowledgementMessage["service"]
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementQueue, acknowledgementMessage)
		else:
			self.acknowledge_failure(acknowledgementQueue, acknowledgementMessage)

	def remove_tomcat_virtual_host(self, stomp_message):
		print("RemoveTomcatVirtualHost - tomcat_virtual_host_service_controller.remove_tomcat_virtual_host()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessage = stomp_message.parsed_body
		acknowledgementQueue = acknowledgementMessage["service"]
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementQueue, acknowledgementMessage)
		else:
			self.acknowledge_failure(acknowledgementQueue, acknowledgementMessage)

	def enable_tomcat_virtual_host(self, stomp_message):
		print("EnableTomcatVirtualHost - tomcat_virtual_host_service_controller.enable_tomcat_virtual_host()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessage = stomp_message.parsed_body
		acknowledgementQueue = acknowledgementMessage["service"]
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementQueue, acknowledgementMessage)
		else:
			self.acknowledge_failure(acknowledgementQueue, acknowledgementMessage)

	def disable_tomcat_virtual_host(self, stomp_message):
		print("DisableTomcatVirtualHost - tomcat_virtual_host_service_controller.disable_tomcat_virtual_host()")
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
