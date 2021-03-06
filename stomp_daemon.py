#!/usr/bin/env python
# stomp_daemon.py
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
from stomp_daemon_config import StompDaemonConfig
from stomp_daemon_connection import StompDaemonConnection
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
###############################################################
app_dir = os.path.abspath(os.path.dirname(sys.argv[0]))
print("Application Dir - " + app_dir)

# Load the configuration file
global stompDaemonConfig
stompDaemonConfig = StompDaemonConfig('config.json', 'processors.json')

# Create a Thread Pool for Provisioning Tasks
# async safe task only
global threadPool
threadPoolCount = 16
threadPool = ThreadPoolExecutor(threadPoolCount)

# Define Message Router as global
# the route table will be populated with references to StompMEssageController's by the StompMessageProcessor constructor
global stompMessageRouter
stompMessageRouter = StompMessageRouter()

# Define the Stomp Connection and Listener as global
# these will be factoried in the StompConnect method
global stompDaemonConnection
stompDaemonConnection = StompDaemonConnection(stompDaemonConfig.msgSrvr, stompDaemonConfig.msgSrvrPort, stompDaemonConfig.msgSrvrClientId)
global stompDaemonListener
stompDaemonListener = StompDaemonListener(stompMessageRouter, threadPool)


# Processors for valid recv_msg_types
#msg_type_processors = {"TN": Task.notification,
#                       "TSQ": Task.statusQuery,
#                       "TSU": Task.statusUpdate}
# Message Processor correspond to subdir's of Message Controllers
global message_processors
message_processors = {}
# Factory StompRegistrationProcessor - Register, Unregister, SendPeerList
message_processors['stomp_registration_processor'] = StompMessageProcessor("stomp_registration_processor", stompMessageRouter, stompDaemonConnection)
# Factory NameServiceManagementProcessor
message_processors['name_service_management_processor'] = StompMessageProcessor("name_service_management_processor", stompMessageRouter, stompDaemonConnection)
# Factory VirtualHostManagementProcessor
message_processors['virtual_host_management_processor'] = StompMessageProcessor("virtual_host_management_processor", stompMessageRouter, stompDaemonConnection)
# Factory VirtualMailManagementProcesor
message_processors['virtual_mail_management_processor'] = StompMessageProcessor("virtual_mail_management_processor", stompMessageRouter, stompDaemonConnection)
# Factory DatabaseManagementProcesor
message_processors['database_management_processor'] = StompMessageProcessor("database_management_processor", stompMessageRouter, stompDaemonConnection)
# Factory TomcatManagementProcesor
message_processors['tomcat_management_processor'] = StompMessageProcessor("tomcat_management_processor", stompMessageRouter, stompDaemonConnection)
# Factory GoogleServiceProcessor
message_processors['google_service_processor'] = StompMessageProcessor("google_service_processor", stompMessageRouter, stompDaemonConnection)

def daemonize( pidfile, *, stdin='/dev/null',
                        stdout='/dev/null',
                        stderr='/dev/null'):
    
    # Already running if pid file exists - SysV-Init
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
        # TODO: Have threads completed before system exit? Need Process Control!
        stompDaemonConnection.stompUnsubscribe(stompDaemonConfig.msgSrvrQueue)
        stompDaemonConnection.stompConn.remove_listener('StompDaemonListener')        
        stompDaemonConnection.stompDisconnect()
        sys.stdout.write('Daemon ended with pid - {0} - {1}\n'.format(os.getpid(), time.ctime()))
        print()
        raise SystemExit(1)
    
    signal.signal(signal.SIGTERM, sigterm_handler)
    
def main():

    print()
    sys.stdout.write('Daemon started with pid - {0} - {1}\n'.format(os.getpid(), time.ctime()))
    #print()

    # Print Routes
    stompMessageRouter.print_routes()

    # Declare stompConn global - allows the sigterm_handler to access and close the connection
    # Factory the Stomp Connection
    # Currently StompConnection11 class default
    # StompConnection12 possible but may not be implemented for all platforms
    # Python Stomp version matching ActiveMQ/Stomp, Rails ActiveMessaging/Stomp, Java JMS/Stomp, WebSockets/Stomp
    stompDaemonConnection.stompConnect(stompDaemonListener)

    # Subscribe to the message queue
    stompDaemonConnection.stompSubscribe(stompDaemonConfig.msgSrvrQueue)

    # Send the CLI start message to itself
    #    stompConn.send(body=' '.join(sys.argv[1:]), destination=msgSrvrQueue)
    # Endless Loop until sigterm
    while True:
#       sys.stdout.write('Daemon Alive! {}\n'.format(time.ctime()))
        time.sleep(60)
        if stompDaemonConnection.stompConn.is_connected():
           print('Agent Connected when daemon wokeup')
        else:
            print('Agent Disconnected when daemon wokeup')
            print('Removing Listener')
            stompDaemonConnection.stompConn.remove_listener('StompDaemonListener')
            print('Disconnecting')
            stompDaemonConnection.stompDisconnect()
            print('Attempting to reconnect')
            stompDaemonConnection.stompConnect(stompDaemonListener)
            print('Attempting to resubscribe')
            stompDaemonConnection.stompSubscribe(stompDaemonConfig.msgSrvrQueue)

                    
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
        
    
    
    
    
    
    
            
