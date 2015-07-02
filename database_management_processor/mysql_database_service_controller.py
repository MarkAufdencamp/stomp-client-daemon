from stomp_message_controller import StompMessageController
from stomp_message import StompMessage

class MysqlDatabaseServiceController(StompMessageController):
	
	stomp_tasks = ["CreateMySQLDatabase", "RemoveMySQLDatabase", "EnableMySQLDatabase", "DisableMySQLDatabase", "SetMySQLDatabasePasswd", "BackupMySQLDatabase", "RestoreMySQLDatabase"]
	
	def run(self):
		print("MysqlDatabaseServiceController")

	def create_my_s_q_l_database(self, stomp_message):
		print("CreateMySQLDatabase - mysql_database_service_controller.create_my_s_q_l_database()")
		stomp_message.print_message()

	def remove_my_s_q_l_database(self, stomp_message):
		print("RemoveMySQLDatabase - mysql_database_service_controller.remove_my_s_q_l_database()")
		stomp_message.print_message()

	def enable_my_s_q_l_database(self, stomp_message):
		print("EnableMySQLDatabase - mysql_database_service_controller.enable_my_s_q_l_database()")
		stomp_message.print_message()

	def disable_my_s_q_l_database(self, stomp_message):
		print("DisableMySQLDatabase - mysql_database_service_controller.disable_my_s_q_l_database()")
		stomp_message.print_message()

	def set_my_s_q_l_database_passwd(self, stomp_message):
		print("SetMySQLDatabasePasswd - mysql_database_service_controller.set_my_s_q_l_database_passwd()")
		stomp_message.print_message()

	def backup_my_s_q_l_database(self, stomp_message):
		print("BackupMySQLDatabase - mysql_database_service_controller.backup_my_s_q_l_database()")
		stomp_message.print_message()

	def restore_my_s_q_l_database(self, stomp_message):
		print("RestoreMySQLDatabase - mysql_database_service_controller.restore_my_s_q_l_database()")
		stomp_message.print_message()
