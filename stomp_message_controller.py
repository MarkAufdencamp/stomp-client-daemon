class StompMessageController:
	def register_stomp_tasks(self, stomp_processor):
		for task in self.stomp_tasks:
			stomp_processor.route_add(task, self)

	def unregister_stomp_tasks(self, stomp_processor):
		for task in self.stomp_tasks:
			stomp_processor.route_delete(task)

	def print_stomp_tasks(self):
		for task in self.stomp_tasks:
			print(" " + task)


class StompMessage:
	def __init__(self, message):
		self.message = message

	def message_header(self):
		print("Message Header")

	def message_body(self):
		print("Mesage Body")

	def stomp_message(self):
		print("Stomp Message")
