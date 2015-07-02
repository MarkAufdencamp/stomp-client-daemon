import json
import inflection

class StompMessageRouter:
	def __init__(self):
		#print("StompMessageRouter constructor")
		self.routes = {}

	def add_routes(self, processor, tasks):
		for task in tasks:
			controller = tasks[task]
			self.routes[task] = tasks[task]

	def delete_routes(self, tasks):
		for task in tasks:
			del self.routes[task]

	def route(self, task):
		return self.routes[task]

	def print_routes(self):
		print("================= Routes =================")
		for task in self.routes:
			print(task, self.routes[task])
		print()

	def route_message(self, task, message):
		#print("Task - {0}".format(task))
		controller = self.routes[task]
		#print("Controller - {0}".format(controller))
		method_name = inflection.underscore(task)
		#print("Method Name - {0}".format(method_name))
		#TODO: try/except getattr
		method = getattr(controller, method_name)
		#print("Method - {0}".format(method))
		method(message)
