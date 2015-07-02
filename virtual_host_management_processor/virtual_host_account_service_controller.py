from stomp_message_controller import StompMessageController
from stomp_message import StompMessage

class VirtualHostAccountServiceController(StompMessageController):

	stomp_tasks = ["CreateVirtualHostAccount", "RemoveVirtualHostAccount", "EnableVirtualHostAcount", "DisableVirtualHostAccount", "SetVirtualHostAccountPasswd", "BackupVirtualHostAccount", "RestoreVirtualHostAccount", "AddSSHAuthorizedKey", "RemoveSSHAuthorizedKey", "AddCRONJob", "RemoveCRONJob"]

	def run(self):
		print( "VirtualHostAccountController" )

	def create_virtual_host_account(self, stomp_message):
		print("CreateVirtualHostAccount - virtual_host_account_service_controller.create_virtual_host_account()")
		stomp_message.print_message()

	def remove_virtual_host_account(self, stomp_message):
		print("RemoveVirtualHostAccount - virtual_host_account_service_controller.remove_virtual_host_account()")
		stomp_message.print_message()

	def enable_virtual_host_account(self, stomp_message):
		print("EnableVirtualHostAccount - virtual_host_account_service_controller.enable_virtual_host_account()")
		stomp_message.print_message()

	def disable_virtual_host_account(self, stomp_message):
		print("DisableVirtualHostAccount - virtual_host_account_service_controller.disable_virtual_host_account()")
		stomp_message.print_message()

	def set_virtual_host_account_passwd(self, stomp_message):
		print("SetVirtualHostAccountPasswd - virtual_host_account_service_controller.set_virtual_host_account_passwd()")
		stomp_message.print_message()

	def backup_virtual_host_account(self, stomp_message):
		print("BackupVirtualHostAccount - virtual_host_account_service_controller.backup_virtual_host_account()")
		stomp_message.print_message()

	def restore_virtual_host_account(self, stomp_message):
		print("RestoreVirtualHostAccount - virtual_host_account_service_controller.restore_virtual_host_account()")
		stomp_message.print_message()

	def add_s_s_h_authorized_key(self, stomp_message):
		print("AddSSHAuthorizedKey - virtual_host_account_service_controller.add_s_s_h_authorized_key()")
		stomp_message.print_message()

	def remove_s_s_h_authorized_key(self, stomp_message):
		print("RemoveSSHAuthorizedKey - virtual_host_account_service_controller.remove_s_s_h_authorized_key()")
		stomp_message.print_message()

	def add_c_r_o_n_job(self, stomp_message):
		print("AddCRONJob - virtual_host_account_service_controller.add_c_r_o_n_job()")
		stomp_message.print_message()

	def remove_c_r_o_n_job(self, stomp_message):
		print("RemoveCRONJob - virtual_host_account_service_controller.remove_c_r_o_n_job()")
		stomp_message.print_message()

