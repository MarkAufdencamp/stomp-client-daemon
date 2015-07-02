import time
import json

class StompMessage:
	def __init__(self, headers, body):
		self.stomp_message_headers = headers
		self.stomp_message_body = body
		self.parse_body()

	def message_headers(self):
		print("Message Header")
		return self.stomp_message_headers

	def message_body(self):
		print("Mesage Body")
		return self.stomp_message_body

	def parse_body(self):
		try:
			self.parsed_body = json.loads(self.stomp_message_body)
		except Exception:
			print("Error parsing StompMessage body.")
			
	def task(self):
		try:
			task = self.parsed_body["task"]
		except KeyError:
			print("Error retrieving StompMessage Task.")
		return task

	def print_message(self):
		print()
		self.print_headers()
		print()
		self.print_body()
		print()
		self.print_parsed_body()
		print()
		print("===========================================================")
		
	def print_headers(self):
		print("== Message Headers (ActiveMQ/Stomp) ==")
		for key in self.stomp_message_headers:
			key_name = key
			key_value = self.stomp_message_headers[key_name]
			print("{0}: {1}".format(key_name, key_value))

	def print_body(self):
		print("== Message Body (json encoded text object) ==")
		print(self.stomp_message_body)

	def print_parsed_body(self):
		print("== Parsed Body (json decoded python dict) ==")
		print(self.parsed_body)
