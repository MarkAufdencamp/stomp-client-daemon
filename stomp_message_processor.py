# Dynamic Class Loader of ./{#}_controllers/ sub dir's
# https://lextoumbourou.com/blog/posts/dynamically-loading-modules-and-classes-in-python/
#
# Controllers should be subclass of StompMessageController
# StompMessageProcessor loads classes from disk and instantiates an instance
# StompMessageController registers controller Tasks with StompMessageProcessor 

import pkgutil
import sys
import os

from stomp_message_controller import StompMessageController
from stomp_message_controller import StompMessage

class StompMessageProcessor:

	# Build class name from module file name
	def get_class_name(self, mod_name):
		output = ""
		words = mod_name.split("_")[0:]
		for word in words:
			output += word.title()
		return output

	# Load class instance
	def load_stomp_controller_class(self, loaded_mod, class_name):
		loaded_class = getattr(loaded_mod, class_name)
		#TODO: Test that loaded class is inherited from StompMessageController
		#TODO: Throw exception if loaded class not inherited from StompMessageController
		instance = loaded_class()
		return instance

	# Load modules from dir
	# Build class name from module file name
	# Instantiate an instance of the class
	# Execute the controller initialize method
	def load_stomp_controllers(self, controller_dir):
		print("Loading controllers - " + controller_dir)
		#TODO: Validate controller_dir existence
		#path = os.path.join(os.path.dirname(__file__), controller_dir)
		#path = os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), controller_dir)
		path = controller_dir
		modules = pkgutil.iter_modules(path=[path])
		for loader, mod_name, ispkg in modules:
			#TODO: Wrap class loader with exception handling
			loaded_mod = __import__(path+"."+ mod_name, fromlist=[mod_name])
			class_name = self.get_class_name(mod_name)
			#TODO: Wrap class instantiation with exception handler
			instance = self.load_stomp_controller_class(loaded_mod, class_name)

			instance.run()
			instance.register_stomp_tasks(self)
			#instance.print_stomp_tasks()

	def reload_stomp_controller():
		print("Reload Stomp controller not yet implemented")

	def print_routes(self):
		for task in self.processor_tasks:
			print(task, self.processor_tasks[task])

	def route_add(self, task, controller):
		#TODO: Validate Task has not been registered by another controller
		self.processor_tasks[task] = controller

	def route_delete(self, task):
		del self.processor_tasks[task]

	def __init__(self, controller_dir):
		# Load Controllers
		self.controller_dir = controller_dir
		self.processor_tasks = dict()
		self.load_stomp_controllers(controller_dir)


#TODO: Read and parse CLI arguments

# Define controller subdir
#controller_dir = "stomp_message_controllers"
#stompProcessor = StompMessageProcessor(controller_dir)
#stompProcessor.print_routes()

# Define constroller subdir
#controller_dir = "virtual_host_management_controllers"
#stompProcessor = StompMessageProcessor(controller_dir)
#stompProcessor.print_routes()

# Define constroller subdir
#controller_dir = "virtual_mail_management_controllers"
#stompProcessor = StompMessageProcessor(controller_dir)
#stompProcessor.print_routes()
