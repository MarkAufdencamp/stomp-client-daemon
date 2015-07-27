import sys
import time
import stomp
from stomp_daemon_listener import StompDaemonListener

class StompDaemonConnection():

# self.msgSrvr
# self.msgSrvrPort
# self.msgSrvrClientId
# self.msgSrvrQueues
# self.stompConn
# self.stompDaemonListener

	def __init__(self, msgSrvr, msgSrvrPort, msgSrvrClientId):
		print("StompDaemonConnection constructor")
		self.msgSrvr = msgSrvr
		self.msgSrvrPort = msgSrvrPort
		self.msgSrvrClientId = msgSrvrClientId
		self.msgSrvrQueues = []

	def stompConnect(self, stompDaemonListener):
		# Connect via Stomp to the Message Server
		# Factory Stomp connection
		sys.stdout.write('Connecting to message server - {0}:{1} {2} - {3}\n'.format(self.msgSrvr, self.msgSrvrPort, self.msgSrvrClientId, time.ctime()))

		try:
			self.stompConn = stomp.Connection( host_and_ports=[(self.msgSrvr, self.msgSrvrPort)], heartbeats=(60000, 20000) )
			self.stompDaemonListener = stompDaemonListener
			self.stompConn.set_listener('StompDaemonListener', stompDaemonListener)
		except Exception as err:
			print('Message Server Connection Error')

		try:
			self.stompConn.start()
		except Exception:
			print('Message Server Start Error')

		try:
			self.stompConn.connect(headers={'client-id': self.msgSrvrClientId})
		except Exception:
			print('Message Server Connect Error')

	def stompDisconnect(self):
		sys.stdout.write('Disconnecting from message server {}\n'.format(time.ctime()))
		#TODO: Remove Listener
		try:
			self.stompConn.disconnect()
		except Exception:
			print('Message Server Disconnect Error')

	def stompSubscribe(self, msgSrvrQueue):
		# Subscribe to the configured message queue
		sys.stdout.write('Subscribing to message queue - {0} - {1}\n'.format(msgSrvrQueue, time.ctime()))
		try:
			self.stompConn.subscribe(destination=msgSrvrQueue, id=1, ack='auto')
			if (msgSrvrQueue not in self.msgSrvrQueues):
				self.msgSrvrQueues.append(msgSrvrQueue)
		except Exception:
			print("Message Queue Subscribe Error")

	def stompUnsubscribe(self, msgSrvrQueue):
		# Unsubscribe to the configured message queue
		sys.stdout.write('Unsubscribing from message queue - {0} - {1}\n'.format(msgSrvrQueue, time.ctime()))
		try:
			self.stompConn.unsubscribe(id=msgSrvrQueue)
			if (msgSrvrQueue in self.msgSrvrQueues):
				self.msgSrvrQueues.remove(msgSrvrQueue)
		except Exception:
			print("Message Queue Unsubscribe Error")

	def stompSendMessage(self, msgSrvrQueue, stompMessage):
		print("StompDaemonConnection stompSendMessage")	