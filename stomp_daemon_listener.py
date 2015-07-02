import time
from concurrent.futures import ThreadPoolExecutor
from stomp import ConnectionListener
from stomp_message import StompMessage

class StompDaemonListener(ConnectionListener):

    def __init__(self, router, threadPool):
        #print("StompDaemonListener constructor")
        super().__init__()
        self.router = router
        self.threadPool = threadPool
        self.recv_msg_types = {"TN": "Task Notification Message Type, Message Id key, Message contains Task Retrieval URL",
                  "TSQ": "Task Status Query Message Type, Message Id key, Message contains Task Notification Message Id"}

    def on_connecting(self, host_and_port):
        print("Agent Connecting")
        
    def on_connected(self, headers, body):
        print("Agent Connected")
        print()
        
    def on_disconnected(self):
        print('Agent Disconnected')
    
    def on_heartbeat_timeout(self):
        print("Agent Heartbeat Timeout")

    # Invoking print() causes a thread exception  
#    def on_before_message(self, headers, body):
#        print("Before Message")
    
    def on_message(self, headers, body):
        print()
        print('Agent Message Received - {0} - {1}'.format(headers['message-id'], time.ctime()))
        self.threadPool.submit(self.msgHandler, headers, body)
        
    def on_error(self, headers, body):
    	#TODO: Walk headers and print key/value pairs
        print('Agent Error Received - {0}'.format(time.ctime()))
        self.threadPool.submit(self.errHandler, headers, body)

    def on_receipt(self, headers, body):
    	#TODO: Walk headers and print key/value pairs
        print('Agent Receipt Received - {0}'.format(time.ctime()))
        self.threadPool.submit(self.receiptHandler, headers, body)
        
    # Invoking print() breaks daemon shutdown sequence error
#    def on_send(self, frame):
#        print("Send")
    
    def on_heartbeat(self):
        print("Agent Heartbeat Received")
        
    def msgHandler(self, headers, body):
        print()
        print('Message process begin - {0} - {1}'.format(headers['message-id'], time.ctime()))
        print("===========================================================")

        try:
            msgType = headers['type']
        except KeyError:
            self.print_msg("INVALID MESSAGE - NO MESSAGE TYPE", headers, body)

        try:
            recvMsg = self.recv_msg_types[msgType]
            #self.print_msg("VALID MESSAGE", headers, body)
        except KeyError:
            self.print_msg("INVALID MESSAGE", headers, body)
    
        try:
            self.route_msg(headers, body)
        except Exception:
            print("StompDaemonListener Routing Exception")

        print('Message process complete - {0} - {1}'.format(headers['message-id'], time.ctime()))
        print()
        
    def errHandler(self, headers, body):
        print_msg("ERROR", headers, body)

    def receiptHandler(self, headers, body):
        print_msg("RECEIPT", headers, body)

    def print_msg(self, frame_type, headers, body):
        print('{0} - {1}'.format(frame_type, time.ctime()))
        for header_key in headers.keys():
            print('{0}: {1}'.format(header_key, headers[ header_key ]))
        print()
        print(body)
        print()

    def route_msg(self, headers, body):
        #print("StompDaemonListener - Route Message")
        try:
             msg = StompMessage(headers, body)
             #print("StompMessage Factoried.")
        except Error:
             print("Error parsing stomp message body.")
     
        try:
            task = msg.task()
            #print("Requested Task - {0}".format(task))
            self.router.route_message(task, msg)
        except Error:
            print("Error routing stomp message.")
#        self.print_msg("Routing Message - ", headers, body)

