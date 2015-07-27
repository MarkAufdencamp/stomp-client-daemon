# StompMessageBroker is a proxy class of StompDaemonConnection with only a sendMessage method
# This exposes a simple interface for a StompMessageController method to communicate via the broker
class StompMessageBroker():
	def __init__(self, stomp_daemon_connection):
		self.stomp_daemon_connection = stomp_daemon_connection
	
	def sendMessage(self, message, queue):
		print("stomp_message_broker.sendMessage() - {0} - {1}".format(queue, message))
		#print(self.stomp_daemon_connection)
		self.stomp_daemon_connection.stompConn.send(queue, message)
		
	def brokerId():
		return self.stomp_daemon_connection.msgSrvrClientId