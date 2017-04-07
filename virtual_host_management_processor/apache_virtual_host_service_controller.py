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
		
		acknowledgementMessageDict = stomp_message.parsed_body
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementMessageDict)
		else:
			self.acknowledge_failure(acknowledgementMessageDict)

	def remove_apache_virtual_host(self, stomp_message):
		print("RemoveApacheVirtualHost - apache_virtual_host_service_controller.remove_apache_virtual_host()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessageDict = stomp_message.parsed_body
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementMessageDict)
		else:
			self.acknowledge_failure(acknowledgementMessageDict)

	def enable_apache_virtual_host(self, stomp_message):
		print("EnableApacheVirtualHost - apache_virtual_host_service_controller.enable_apache_virtual_host()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessageDict = stomp_message.parsed_body
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementMessageDict)
		else:
			self.acknowledge_failure(acknowledgementMessageDict)

	def disable_apache_virtual_host(self, stomp_message):
		print("DisableApacheVirtualHost - apache_virtual_host_service_controller.disable_apache_virtual_host()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessageDict = stomp_message.parsed_body
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementMessageDict)
		else:
			self.acknowledge_failure(acknowledgementMessageDict)

	def create_apache_virtual_host_proxy(self, stomp_message):
		print("CreateApacheVirtualHostProxy - apache_virtual_host_service_controller.create_apache_virtual_host_proxy()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessageDict = stomp_message.parsed_body
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementMessageDict)
		else:
			self.acknowledge_failure(acknowledgementMessageDict)

	def remove_apache_virtual_host_proxy(self, stomp_message):
		print("RemoveApacheVirtualHostProxy - apache_virtual_host_service_controller.remove_apache_virtual_host_proxy()")
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
