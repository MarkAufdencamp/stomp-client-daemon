from stomp_message_controller import StompMessageController
from stomp_message import StompMessage

class MysqlDatabaseServiceController(StompMessageController):
	
	stomp_tasks = ["CreateMySQLDatabase", "RemoveMySQLDatabase", "EnableMySQLDatabase", "DisableMySQLDatabase", "SetMySQLDatabasePasswd", "BackupMySQLDatabase", "RestoreMySQLDatabase"]
	
	def run(self):
		print("MysqlDatabaseServiceController")

	def create_my_sql_database(self, stomp_message):
		print("CreateMySQLDatabase - mysql_database_service_controller.create_my_sql_database()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessageDict = stomp_message.parsed_body
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementMessageDict)
		else:
			self.acknowledge_failure(acknowledgementMessageDict)

	def remove_my_sql_database(self, stomp_message):
		print("RemoveMySQLDatabase - mysql_database_service_controller.remove_my_sql_database()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessageDict = stomp_message.parsed_body
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementMessageDict)
		else:
			self.acknowledge_failure(acknowledgementMessageDict)

	def enable_my_sql_database(self, stomp_message):
		print("EnableMySQLDatabase - mysql_database_service_controller.enable_my_sql_database()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessageDict = stomp_message.parsed_body
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementMessageDict)
		else:
			self.acknowledge_failure(acknowledgementMessageDict)

	def disable_my_sql_database(self, stomp_message):
		print("DisableMySQLDatabase - mysql_database_service_controller.disable_my_sql_database()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessageDict = stomp_message.parsed_body
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementMessageDict)
		else:
			self.acknowledge_failure(acknowledgementMessageDict)

	def set_my_sql_database_passwd(self, stomp_message):
		print("SetMySQLDatabasePasswd - mysql_database_service_controller.set_my_sql_database_passwd()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessageDict = stomp_message.parsed_body
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementMessageDict)
		else:
			self.acknowledge_failure(acknowledgementMessageDict)

	def backup_my_sql_database(self, stomp_message):
		print("BackupMySQLDatabase - mysql_database_service_controller.backup_my_sql_database()")
		stomp_message.print_message()

		successfulProvisioning = True
		
		acknowledgementMessageDict = stomp_message.parsed_body
		
		if successfulProvisioning:
			self.acknowledge_success(acknowledgementMessageDict)
		else:
			self.acknowledge_failure(acknowledgementMessageDict)

	def restore_my_sql_database(self, stomp_message):
		print("RestoreMySQLDatabase - mysql_database_service_controller.restore_my_sql_database()")
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
