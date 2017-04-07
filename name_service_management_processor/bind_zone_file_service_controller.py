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
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementMessageDict)
		else:
			self.acknowledge_failure(acknowledgementMessageDict)

	def remove_bind_zone_file(self, stomp_message):
		print("RemoveBindZone - bind_zone_file_service_controller.remove_bind_zone_file()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessageDict = stomp_message.parsed_body
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementMessageDict)
		else:
			self.acknowledge_failure(acknowledgementMessageDict)

	def enable_bind_zone_file(self, stomp_message):
		print("EnableBindZone - bind_zone_file_service_controller.enable_bind_zone_file()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessageDict = stomp_message.parsed_body
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementMessageDict)
		else:
			self.acknowledge_failure(acknowledgementMessageDict)

	def disable_bind_zone_file(self, stomp_message):
		print("DisableBindZone - bind_zone_file_service_controller.disable_bind_zone_file()")
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
