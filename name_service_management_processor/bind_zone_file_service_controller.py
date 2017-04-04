from stomp_message_controller import StompMessageController
from stomp_message import StompMessage

class BindZoneFileServiceController(StompMessageController):
	
	stomp_tasks = ["CreateBindZoneFile", "RemoveBindZoneFile", "EnableBindZoneFile", "DisableBindZoneFile"]
	
	def run(self):
		print("BindZoneFileServiceController")

	def create_bind_zone_file(self, stomp_message):
		print("CreateBindZoneFile - bind_zone_file_service_controller.create_bind_zone_file()")
		stomp_message.print_message()
		
		successfulProvisioning = True
		
		acknowledgementMessageDict = stomp_message.parsed_body
		acknowledgementQueue = acknowledgementMessageDict["service"]
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementQueue, acknowledgementMessageDict)
		else:
			self.acknowledge_failure(acknowledgementQueue, acknowledgementMessageDict)

	def remove_bind_zone_file(self, stomp_message):
		print("RemoveBindZone - bind_zone_file_service_controller.remove_bind_zone_file()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessage = stomp_message.parsed_body
		acknowledgementQueue = acknowledgementMessage["service"]
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementQueue, acknowledgementMessage)
		else:
			self.acknowledge_failure(acknowledgementQueue, acknowledgementMessage)

	def enable_bind_zone_file(self, stomp_message):
		print("EnableBindZone - bind_zone_file_service_controller.enable_bind_zone_file()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessage = stomp_message.parsed_body
		acknowledgementQueue = acknowledgementMessage["service"]
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementQueue, acknowledgementMessage)
		else:
			self.acknowledge_failure(acknowledgementQueue, acknowledgementMessage)

	def disable_bind_zone_file(self, stomp_message):
		print("DisableBindZone - bind_zone_file_service_controller.disable_bind_zone_file()")
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
