class StompDaemonConnection():
	def __init__(self):
		print("StompDaemonConnection constructor")

	def stompConnect(self, msgSrvr, msgSrvrPort, msgSrvrClientId, stompMessageRouter, threadPool):
		# Connect via Stomp to the Message Server
		# Factory Stomp connection
		sys.stdout.write('Connecting to message server - {0}:{1} - {2}\n'.format(msgSrvr, msgSrvrPort, time.ctime()))
		global stompConn, stompDaemonListener

		try:
			stompConn = stomp.Connection( host_and_ports=[(msgSrvr, msgSrvrPort)], heartbeats=(60000, 20000) )
			stompDaemonListener = StompDaemonListener(stompMessageRouter, threadPool)
			stompConn.set_listener('StompDaemonListener', stompDaemonListener)
		except Exception as err:
			print('Message Server Connection Error')

		try:
			stompConn.start()
		except Exception:
			print('Message Server Start Error')

		try:
			stompConn.connect(headers={'client-id': msgSrvrClientId})
		except Exception:
			print('Message Server Connect Error')

	def stompDisconnect(self, stompConn):
		sys.stdout.write('Disconnecting from message server {}\n'.format(time.ctime()))
		try:
			stompConn.disconnect()
		except Exception:
			print('Message Server Disconnect Error')

	def stompSubscribe(self, stompConn, msgSrvrQueue):
		# Subscribe to the configured message queue
		sys.stdout.write('Subscribing to message queue - {0} - {1}\n'.format(msgSrvrQueue, time.ctime()))
		try:
			stompConn.subscribe(destination=msgSrvrQueue, id=1, ack='auto')
		except Exception:
			print("Message Queue Subscribe Error")

	def stompUnsubscribe(self, stompConn, msgSrvrQueue):
		# Unsubscribe to the configured message queue
		sys.stdout.write('Unsubscribing from message queue - {0} - {1}\n'.format(msgSrvrQueue, time.ctime()))
		try:
			stompConn.unsubscribe(id=msgSrvrQueue)
		except Exception:
			print("Message Queue Unsubscribe Error")


