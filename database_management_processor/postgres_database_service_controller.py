from stomp_message_controller import StompMessageController
from stomp_message import StompMessage

class PostgresDatabaseServiceController(StompMessageController):
	
	stomp_tasks = ["CreatePostgresDatabase", "RemovePostgresDatabase", "EnablePostgresDatabase", "DisablePostgresDatabase", "SetPostgresDatabasePasswd", "BackupPostgresDatabase", "RestorePostgresDatabase"]
	
	def run(self):
		print("PostgresDatabaseServiceController")

	def create_postgres_database(self, stomp_message):
		print("CreatePostgresDatabase - postgres_database_service_controller.create_postgres_database()")
		stomp_message.print_message()

	def remove_postgres_database(self, stomp_message):
		print("RemovePostgresDatabase - postgres_database_service_controller.remove_postgres_database()")
		stomp_message.print_message()

	def enable_postgres_database(self, stomp_message):
		print("EnablePostgresDatabase - postgres_database_service_controller.enable_postgres_database()")
		stomp_message.print_message()

	def disable_postgres_database(self, stomp_message):
		print("DisablePostgresDatabase - postgres_database_service_controller.disable_postgres_database()")
		stomp_message.print_message()

	def set_postgres_database_passwd(self, stomp_message):
		print("SetPostgresDatabasePasswd - postgres_database_service_controller.set_postgres_database_passwd()")
		stomp_message.print_message()

	def backup_postgres_database(self, stomp_message):
		print("BackupPostgresDatabase - postgres_database_service_controller.backup_postgres_database()")
		stomp_message.print_message()

	def restore_postgres_database(self, stomp_message):
		print("RestorePostgresDatabase - postgres_database_service_controller.restore_postgres_database()")
		stomp_message.print_message()
