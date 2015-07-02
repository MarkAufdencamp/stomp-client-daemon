#!/usr/bin/env python
# daemon
# Python 3 Packages
import os
import sys
import atexit
import signal
import time
import queue
import socket
from concurrent.futures import ThreadPoolExecutor
import pprint
# PyPi Packages
# pip -r requirements.txt
import stomp
import json
# Local imports
from stomp_daemon_listener import StompDaemonListener
from stomp_message import StompMessage
from stomp_message_processor import StompMessageProcessor
from stomp_message_controller import StompMessageController
from stomp_message_router import StompMessageRouter

# Credits:
#    Python Cookbook - 12.14 Launching a Daemon Process on Unix
#    Stomp.py - https://github.com/jasonrbriggs/stomp.py
#    https://twiki.cern.ch/twiki/bin/view/EGEE/MsgTutorial
#
# Load the configuration file
config = json.load(open('config.json'))
app_dir = os.path.abspath(os.path.dirname(sys.argv[0]))

# Create a Thread Pool for Provisioning Tasks
global threadPool
threadPoolCount = 16
threadPool = ThreadPoolExecutor(threadPoolCount)

# Processors for valid recv_msg_types
#msg_type_processors = {"TN": Task.notification,
#                       "TSQ": Task.statusQuery,
#                       "TSU": Task.statusUpdate}

global stompConn, stompDaemonListener
msgSrvr="localhost"
msgSrvrPort=61613
msgSrvrQueue="/queue/stomp-message-processor-server.local"
msgSrvrClientId="stomp-message-processor-server.local"

#
print("Application Dir - " + app_dir)

global stompMessageRouter
stompMessageRouter = StompMessageRouter()

# Message Processor correspond to subdir's of Message Controllers
global message_processors
message_processors = {}
# Factory StompRegistrationProcessor - Register, Unregister, SendPeerList
message_processors['stomp_registration_processor'] = StompMessageProcessor("stomp_registration_processor", stompMessageRouter)
# Factory NameServiceManagementProcessor
message_processors['name_service_management_processor'] = StompMessageProcessor("name_service_management_processor", stompMessageRouter)
# Factory VirtualHostManagementProcessor
message_processors['virtual_host_management_processor'] = StompMessageProcessor("virtual_host_management_processor", stompMessageRouter)
# Factory VirtualMailManagementProcesor
message_processors['virtual_mail_management_processor'] = StompMessageProcessor("virtual_mail_management_processor", stompMessageRouter)
# Factory DatabaseManagementProcesor
message_processors['database_management_processor'] = StompMessageProcessor("database_management_processor", stompMessageRouter)
# Factory TomcatManagementProcesor
message_processors['tomcat_management_processor'] = StompMessageProcessor("tomcat_management_processor", stompMessageRouter)

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
        stompConn.remove_listener('StompDaemonListener')        
        stompDisconnect(stompConn)
        print()
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
        print("Error loading msgSrvrQueue from config.json - Utilizing default - '/queue/stomp-message-server-processor.local'")

    try:
        msgSrvrClientId = config['msgSrvrClientId']
    except KeyError:
        print("Error loading msgSrvrClientId from config.json - Utilizing default - 'stomp-message-processor-server.local'")

    
def validateConfig(config):
    hostname = socket.gethostbyaddr(socket.gethostname())[0]
    ip_addresses = socket.gethostbyname_ex(socket.gethostname())[2]

def printRoutes(stompMessageRouter):
    stompMessageRouter.print_routes()
            
def stompConnect(msgSrvr, msgSrvrPort, stompMessageRouter, threadPool):
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
    print()
    sys.stdout.write('Daemon started with pid - {0} - {1}\n'.format(os.getpid(), time.ctime()))
    print()
    # Parse configuration values - creates global msgSrvr, msgSrvrPort, and msgSrvrQueue
    parseConfig(config)

    # Print Routes
    printRoutes(stompMessageRouter)

    # Declare stompConn global - allows the sigterm_handler to access and close the connection
    # Factory the Stomp Connection
    # Currently StompConnection11 class default
    # StompConnection12 possible but may not be implemented for all platforms
    # Python Stomp version matching ActiveMQ/Stomp, Rails ActiveMessaging/Stomp, Java JMS/Stomp, WebSockets/Stomp
    stompConnect(msgSrvr, msgSrvrPort, stompMessageRouter, threadPool)

    # Subscribe to the message queue
    stompSubscribe(stompConn, msgSrvrQueue)

    # Send the CLI start message to itself
    #    stompConn.send(body=' '.join(sys.argv[1:]), destination=msgSrvrQueue)
    # Endless Loop until sigterm
    while True:
#       sys.stdout.write('Daemon Alive! {}\n'.format(time.ctime()))
        time.sleep(60)
        if stompConn.is_connected():
           print('Agent Connected when daemon wokeup')
        else:
            print('Agent Disconnected when daemon wokeup')
            print('Removing Listener')
            stompConn.remove_listener('StompDaemonListener')
            print('Attempting to reconnect')
            stompDisconnect(stompConn)
            stompConnect(msgSrvr, msgSrvrPort, threadPool)
            print('Attempting to resubscribe')
            stompSubscribe(stompConn, msgSrvrQueue)
#            stompConn.connect(wait=True)
#       stompConn.subscribe(destination=msgSrvrQueue, ack='auto', headers=HEADERS)          

                    
if __name__ == '__main__':
    PIDFILE = '/tmp/stomp_daemon.pid'
        
    if len(sys.argv) != 2:
        print('Usage: {} [start|stop|reload|status'.format(sys.argv[0]), file=sys.stderr)
        raise SystemExit(1)
        
    if sys.argv[1] == 'start':
        try:
            daemonize(PIDFILE,
                          stdout='/tmp/stomp_daemon.log',
                          stderr='/tmp/stomp_daemon.log')
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
        
    
    
    
    
    
    
            
