from stomp_message_controller import StompMessageController
from stomp_message import StompMessage

class DnsDomainServiceController(StompMessageController):
	
	stomp_tasks = ["AddBindZoneARecord", "RemoveBindZoneARecord", "AddBindZoneCNameRecord", "RemoveBindZoneCNameRecord", "AddBindZoneMXRecord", "RemoveBindZoneMXRecord", "AddBindZoneSPFRecord", "RemoveBindZoneSPFRecord"]
	
	def run(self):
		print("DnsDomainServiceController")

	def add_bind_zone_a_record(self, stomp_message):
		print("AddBindZoneARecord - dns_domain_service_controller.add_bind_zone_a_record()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessageDict = stomp_message.parsed_body
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementMessageDict)
		else:
			self.acknowledge_failure(acknowledgementMessageDict)

	def remove_bind_zone_a_record(self, stomp_message):
		print("RemoveBindZoneARecord - dns_domain_service_controller.remove_bind_zone_a_record()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessageDict = stomp_message.parsed_body
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementMessageDict)
		else:
			self.acknowledge_failure(acknowledgementMessageDict)

	def add_bind_zone_c_name_record(self, stomp_message):
		print("AddBindZoneCNameRecord - dns_domain_service_controller.add_bind_zone_c_name_record()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessageDict = stomp_message.parsed_body
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementMessageDict)
		else:
			self.acknowledge_failure(acknowledgementMessageDict)

	def remove_bind_zone_c_name_record(self, stomp_message):
		print("RemoveBindZoneCNameRecord - dns_domain_service_controller.remove_bind_zone_c_name_record()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessageDict = stomp_message.parsed_body
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementMessageDict)
		else:
			self.acknowledge_failure(acknowledgementMessageDict)

	def add_bind_zone_mx_record(self, stomp_message):
		print("AddBindZoneMXRecord - dns_domain_service_controller.add_bind_zone_mx_record()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessageDict = stomp_message.parsed_body
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementMessageDict)
		else:
			self.acknowledge_failure(acknowledgementMessageDict)

	def remove_bind_zone_mx_record(self, stomp_message):
		print("RemoveBindZoneMXRecord - dns_domain_service_controller.remove_bind_zone_mx_record()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessageDict = stomp_message.parsed_body
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementMessageDict)
		else:
			self.acknowledge_failure(acknowledgementMessageDict)

	def add_bind_zone_spf_record(self, stomp_message):
		print("AddBindZoneSPFRecord - dns_domain_service_controller.add_bind_zone_spf_record()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessageDict = stomp_message.parsed_body
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementMessageDict)
		else:
			self.acknowledge_failure(acknowledgementMessageDict)

	def remove_bind_zone_spf_record(self, stomp_message):
		print("RemoveBindZoneSPFRecord - dns_domain_service_controller.remove_bind_zone_spf_record()")
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
