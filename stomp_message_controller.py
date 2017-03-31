import json

class StompMessageController:
	def set_stomp_message_broker(self, stompMessageBroker):
		self.stompMessageBroker = stompMessageBroker

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

	def send_message(self, queue, messageDict):
		print("StompMessageController() send_message")

		jsonMsg = json.dumps(messageDict)
		messageQueue = "/queue/" + queue
		#print(messageQueue)
		#print("Queue - {0}, Clients - {1}".format(messageQueue, self.registeredClients) )

		self.stompMessageBroker.sendMessage(jsonMsg, messageQueue)

	def __getattr__(self, name):
		def _missing(*args, **kwargs):
			print("A missing method was called.")
			print("The Object was {0} and the method was {1}".format(self, name))
			print("It was called with {0} and {1}".format(args, kwargs))
		return _missing