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
		
		acknowledgementMessageDict = stomp_message.parsed_body
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementMessageDict)
		else:
			self.acknowledge_failure(acknowledgementMessageDict)

	def remove_tomcat_virtual_host(self, stomp_message):
		print("RemoveTomcatVirtualHost - tomcat_virtual_host_service_controller.remove_tomcat_virtual_host()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessageDict = stomp_message.parsed_body
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementMessageDict)
		else:
			self.acknowledge_failure(acknowledgementMessageDict)

	def enable_tomcat_virtual_host(self, stomp_message):
		print("EnableTomcatVirtualHost - tomcat_virtual_host_service_controller.enable_tomcat_virtual_host()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessageDict = stomp_message.parsed_body
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementMessageDict)
		else:
			self.acknowledge_failure(acknowledgementMessageDict)

	def disable_tomcat_virtual_host(self, stomp_message):
		print("DisableTomcatVirtualHost - tomcat_virtual_host_service_controller.disable_tomcat_virtual_host()")
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
