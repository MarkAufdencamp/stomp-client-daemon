#!/usr/bin/env python
# daemon
# Python 3 Packages
import os
import sys
import atexit
import signal
import time
import queue
from concurrent.futures import ThreadPoolExecutor
# PyPi Packages
# pip -r requirements.txt
import stomp
from stomp import ConnectionListener
import json

# main()->parseConfig() defines msgSrvr, msgSrvrPort, and msgSrvrQueue as global
# main() defines stompConn as global - allows acces to cleanly close connection on sigterm

# Credits:
#    Python Cookbook - 12.14 Launching a Daemon Process on Unix
#    Stomp.py - https://github.com/jasonrbriggs/stomp.py
#    https://twiki.cern.ch/twiki/bin/view/EGEE/MsgTutorial
#
# Load the configuration file
config = json.load(open('config.json'))

# Create a Thread Pool for Provisioning Tasks
threadPoolCount = 16
threadPool = ThreadPoolExecutor(threadPoolCount)

# Valid Provisioning Task Messages
recv_msg_types = {"TN": "Task Notification, Message contains Task Retrieval URL",
                  "TSQ": "Task Status Query, Message contains Task Notification Message Id"}

send_msg_types  = {"TSU": "Task Status Update, Message contains Task Notification Message Id, Task Sate"}

# Processors for valid recv_msg_types
#msg_type_processors = {"TN": Task.notification,
#                       "TSQ": Task.statusQuery,
#                       "TSU": Task.statusUpdate}

global stompConn
msgSrvr="localhost"
msgSrvrPort=61613
msgSrvrQueue="/queue/localhost"

# Inner Class for Stomp Message Handling
class DaemonStompListener(ConnectionListener):
    def on_connecting(self, host_and_port):
        print("Agent Connecting")
        
    def on_connected(self, headers, body):
        print("Agent Connected")
        
    # The retry eventually breaks the stack
    # Maybe this should fail gracefully without retry and the main daemon loop should test onnectivity on wakeup from sleep
    def on_disconnected(self):
        print('Agent Disconnected')
        print('Attempting to reconnect')
        stompConn.start()
        stompConn.connect(wait=True)
        stompConn.subscribe(destination=msgSrvrQueue, ack='auto', headers=HEADERS)          
    
    def on_heartbeat_timeout(self):
        print("Heartbeat Timeout")

    # Invoking print() causes a thread exception  
#    def on_before_message(self, headers, body):
#        print("Before Message")
    
    def on_message(self, headers, body):
        print('Agent Message Received - {0} - {1}'.format(headers['message-id'], time.ctime()))
        threadPool.submit(self.msgHandler, headers, body)
        
    def on_error(self, headers, body):
        print('Agent Error Received - {0} - {1}'.format(headers['message-id'], time.ctime()))
        threadPool.submit(self.errHandler, headers, body)

    def on_receipt(self, headers, body):
        print('Agent Receipt Received - {} - {}'.format(headers['message-id'], time.ctime()))
        threadPool.submit(self.receiptHandler, headers, body)
        
    # Invoking print() breaks daemon shutdown sequence error
#    def on_send(self, frame):
#        print("Send")
    
    def on_heartbeat(self):
        print("Heartbeat")
        
    def msgHandler(self, headers, body):
        print('Message process begin - {0} - {1}'.format(headers['message-id'], time.ctime()))       

        try:
            msgType = headers['type']
        except KeyError:
            DaemonStompListener.print_msg("INVALID MESSAGE - NO MESSAGE TYPE", headers, body)

        try:
            recvMsg = recv_msg_types[msgType]
            DaemonStompListener.print_msg("VALID MESSAGE", headers, body)
        except KeyError:
            DaemonStompListener.print_msg("INVALID MESSAGE", headers, body)
            
        print('Message process complete - {0} - {1}'.format(headers['message-id'], time.ctime()))
        
    def errHandler(self, headers, body):
        print_msg("ERROR", headers, body)

    def receiptHandler(self, headers, body):
        print_msg("RECEIPT", headers, body)

    def print_msg(frame_type, headers, body):
        print('{0} - {1}'.format(frame_type, time.ctime()))
        for header_key in headers.keys():
            print('{0}: {1}'.format(header_key, headers[ header_key ]))
        print()
        print(body)
        print()
        sys.stdout.flush()
                
def daemonize( pidfile, *, stdin='/dev/null',
                        stdout='/dev/null',
                        stderr='/dev/null'):
    
    # Already running if pid file exist - SysV-Init
    if os.path.exists(pidfile):
        raise RuntimeError('Already running')

    # First fork (detaches from parent)
    try:
        if os.fork() > 0:
            raise SystemExit(0)
    except OSError as e:
            raise RuntimeError('fork #1 failed.')
    
    os.chdir('/')
    os.umask(0)
    os.setsid()
    # Second fork (relinquish session leadership)
    try:
        if os.fork() > 0:
            raise SystemExit(0)
    except OSError as e:
        raise RuntimeError('fork #2 failed.')
    
    # Flush I/O buffers
    sys.stdout.flush()
    sys.stderr.flush()    
    
    # Replace file descriptors for stdin, stdout, and stderr
    with open(stdin, 'rb', 0) as f:
        os.dup2(f.fileno(),sys.stdin.fileno())
    with open(stdout, 'ab', 0) as f:
        os.dup2(f.fileno(),sys.stdout.fileno())
    with open(stderr, 'ab', 0) as f:
        os.dup2(f.fileno(),sys.stderr.fileno())

    # Write the PID file
    with open(pidfile, 'w') as f:
        print( os.getpid(), file=f)
#       print f, os.getpid()
        
   # Arrange to have the PID file removed on exit/signal
    atexit.register(lambda: os.remove(pidfile))

    # Signal handler for termination (required)
    def sigterm_handler(signo, frame):
        stompUnsubscribe(stompConn, msgSrvrQueue)
        stompDisconnect(stompConn)
        sys.stdout.write('Daemon ended with pid - {0} - {1}\n'.format(os.getpid(), time.ctime()))
        raise SystemExit(1)
    
    signal.signal(signal.SIGTERM, sigterm_handler)
    
def parseConfig(config):
    global msgSrvr, msgSrvrPort, msgSrvrQueue    
    try:
        msgSrvr = config['msgSrvr']
    except KeyError:
        print("Error loading msgSrvr from config.json - Utilizing default - 'localhost'")
                
    try:
        msgSrvrPort = config['msgSrvrPort']
    except KeyError:
        print("Error loading msgSrvrPort from config.json - Utilizing default - '61613'")

    try:
        msgSrvrQueue =  config['msgSrvrQueue']
    except KeyError:
        print("Error loading msgSrvrQueue from config.json - Utilizing default - '/queue/localhost'")
    
def stompConnect(msgSrvr, msgSrvrPort):
    # Connect via Stomp to the Message Server
    # Factory Stomp connection
    sys.stdout.write('Connecting to message server - {0}:{1} - {2}\n'.format(msgSrvr, msgSrvrPort, time.ctime()))
    global stompConn
    stompConn = stomp.Connection( host_and_ports=[(msgSrvr, msgSrvrPort)] )
    stompConn.set_listener('DaemonStompListener',DaemonStompListener())
    try:
        stompConn.start()
    except Exception:
        print('Message Server Start Error')
    try:
        stompConn.connect()
    except Exception:
        print('Message Server Connect Error')
 
          
def stompDisconnect(stompConn):
    sys.stdout.write('Disconnecting from message server {}\n'.format(time.ctime()))
    try:
        stompConn.disconnect()
    except Exception:
        print('Message Server Disconnect Error')

def stompSubscribe(stompConn, msgSrvrQueue):
    # Subscribe to the configured message queue
    sys.stdout.write('Subscribing to message queue - {0} - {1}\n'.format(msgSrvrQueue, time.ctime()))
    try:
        stompConn.subscribe(destination=msgSrvrQueue, id=1, ack='auto')
    except Exception:
        print("Message Queue Subscribe Error")

def stompUnsubscribe(stompConn, msgSrvrQueue):
    # Unsubscribe to the configured message queue
    sys.stdout.write('Unsubscribing from message queue - {0} - {1}\n'.format(msgSrvrQueue, time.ctime()))
    try:
        stompConn.unsubscribe(id=msgSrvrQueue)
    except Exception:
        print("Message Queue Unsubscribe Error")
        
def main():
    sys.stdout.write('Daemon started with pid - {0} - {1}\n'.format(os.getpid(), time.ctime()))
    # Parse configuration values - creates global msgSrvr, msgSrvrPort, and msgSrvrQueue
    parseConfig(config)
    # Declare stompConn global - allows the sigterm_handler to access and close the connection
    # Factory the Stomp Connection
    # Currently StompConnection11 class default
    # StompConnection12 possible but may not be implemented for all platforms
    # Python Stomp version matching ActiveMQ/Stomp, Rails ActiveMessaging/Stomp, Java JMS/Stomp, WebSockets/Stomp
    stompConnect(msgSrvr, msgSrvrPort)
    # Subscribe to the message queue
    stompSubscribe(stompConn, msgSrvrQueue)
    # Send the CLI start message to itself
#    stompConn.send(body=' '.join(sys.argv[1:]), destination=msgSrvrQueue)
    # Endless Loop until sigterm
    while True:
#       sys.stdout.write('Daemon Alive! {}\n'.format(time.ctime()))
       time.sleep(10)

                    
if __name__ == '__main__':
    PIDFILE = '/tmp/daemon.pid'
        
    if len(sys.argv) != 2:
        print('Usage: {} [start|stop|reload|status'.format(sys.argv[0]), file=sys.stderr)
        raise SystemExit(1)
        
    if sys.argv[1] == 'start':
        try:
            daemonize(PIDFILE,
                          stdout='/tmp/daemon.log',
                          stderr='/tmp/daemon.log')
        except RuntimeError as e:
            print(e, file=sys.stderr)
            raise SystemExit(1)
        main()
                        
    elif sys.argv[1] == 'stop':
        if os.path.exists(PIDFILE):
            with open(PIDFILE) as f:
                os.kill(int(f.read()), signal.SIGTERM)
        else:
            print('Not running', file=sys.stderr)
            raise SystemExit(1)
                
    elif sys.argv[1] == 'reload':
        print('Pending Implementation - {!r}'.format(sys.argv[1]), file=sys.stderr)
        raise SystemExit(1)
            
    elif sys.argv[1] == 'status':
        print('Pending Implementation - {!r}'.format(sys.argv[1]), file=sys.stderr)
        raise SystemExit(1)
            
    else:
        print('Unknown command {!r}'.format(sys.argv[1]), file=sys.stderr)
        raise SystemExit(1)
        
    
    
    
    
    
    
            