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
		
		acknowledgementMessage = stomp_message.parsed_body
		acknowledgementQueue = acknowledgementMessage["service"]
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementQueue, acknowledgementMessage)
		else:
			self.acknowledge_failure(acknowledgementQueue, acknowledgementMessage)

	def delete_compute_engine_instance(self, stomp_message):
		print("DeleteComputeEngineInstance - google_compute_engine_controller.delete_compute_engine_instance()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessage = stomp_message.parsed_body
		acknowledgementQueue = acknowledgementMessage["service"]
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementQueue, acknowledgementMessage)
		else:
			self.acknowledge_failure(acknowledgementQueue, acknowledgementMessage)

	def start_compute_engine_instance(self, stomp_message):
		print("StartComputeEngineInstance - google_compute_engine_controller.start_compute_engine_instance()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessage = stomp_message.parsed_body
		acknowledgementQueue = acknowledgementMessage["service"]
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementQueue, acknowledgementMessage)
		else:
			self.acknowledge_failure(acknowledgementQueue, acknowledgementMessage)

	def stop_compute_engine_instance(self, stomp_message):
		print("StopComputeEngineInstance - google_compute_engine_controller.stop_compute_engine_instance()")
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
