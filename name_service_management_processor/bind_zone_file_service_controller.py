from stomp_message_controller import StompMessageController
from stomp_message import StompMessage

class BindZoneFileServiceController(StompMessageController):
	
	stomp_tasks = ["CreateBindZoneFile", "RemoveBindZoneFile", "EnableBindZoneFile", "DisableBindZoneFile"]
	
	def run(self):
		print("BindZoneFileServiceController")

	def create_bind_zone_file(self, stomp_message):
		print("CreateBindZoneFile - bind_zone_file_service_controller.create_bind_zone_file()")
		stomp_message.print_message()

	def remove_bind_zone_file(self, stomp_message):
		print("RemoveBindZone - bind_zone_file_service_controller.remove_bind_zone_file()")
		stomp_message.print_message()

	def enable_bind_zone_file(self, stomp_message):
		print("EnableBindZone - bind_zone_file_service_controller.enable_bind_zone_file()")
		stomp_message.print_message()

	def disable_bind_zone_file(self, stomp_message):
		print("DisableBindZone - bind_zone_file_service_controller.disable_bind_zone_file()")
		stomp_message.print_message()
