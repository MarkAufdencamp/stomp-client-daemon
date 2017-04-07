from stomp_message_controller import StompMessageController
from stomp_message import StompMessage
# https://developers.google.com/api-client-library/python/
# google-api-python-client

class GoogleComputeEngineController(StompMessageController):
	
	stomp_tasks = ["CreateComputeEngineInstance", "DeleteComputeEngineInstance", "StartComputeEngineInstance", "StopComputeEngineInstance"]
	
	def run(self):
		print("GoogleComputeEngineController")

	def create_compute_engine_instance(self, stomp_message):
		print("CreateComputeEngineInstance - google_compute_engine_controller.create_compute_engine_instance()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessageDict = stomp_message.parsed_body
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementMessageDict)
		else:
			self.acknowledge_failure(acknowledgementMessageDict)

	def delete_compute_engine_instance(self, stomp_message):
		print("DeleteComputeEngineInstance - google_compute_engine_controller.delete_compute_engine_instance()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessageDict = stomp_message.parsed_body
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementMessageDict)
		else:
			self.acknowledge_failure(acknowledgementMessageDict)

	def start_compute_engine_instance(self, stomp_message):
		print("StartComputeEngineInstance - google_compute_engine_controller.start_compute_engine_instance()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessageDict = stomp_message.parsed_body
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementMessageDict)
		else:
			self.acknowledge_failure(acknowledgementMessageDict)

	def stop_compute_engine_instance(self, stomp_message):
		print("StopComputeEngineInstance - google_compute_engine_controller.stop_compute_engine_instance()")
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
