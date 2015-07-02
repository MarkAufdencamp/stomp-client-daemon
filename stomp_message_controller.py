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

	def print_stomp_message(self, stomp_message):
		print()
		print(stomp_message)
		print()