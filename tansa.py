import socket
import pyfiglet
from colorama import Fore,init
import argparse
import threading
import sys
from contextlib import redirect_stdout
init()

#Banner
sty = pyfiglet.figlet_format("T a n s a",font='ogre')
print(Fore.BLUE + sty)

open_ports = []
threads  = []
lock = threading.Lock()

# Create the argument parser
parser = argparse.ArgumentParser()
# Add arguments
parser.add_argument("-t","--target", help="specify the target",required=True)
parser.add_argument("-p","--port", type=int, nargs='+',help="specify no. of ports")
parser.add_argument("-o","--output" ,help="save the output as txt")
# Parse arguments
args = parser.parse_args()
# Use the arguments
host = args.target
scan_output = args.output
# set timmeout  -- less accurate tho
socket.setdefaulttimeout(0.2)

#scanning function
def scan(host, port):
    # try connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((host,port))

    if result == 0:
            print(f"Port {port} is open")
            with lock:
                 open_ports.append(port)
    s.close()

#scan the port if -p specfied
if args.port is not None:
     ports_to_scan = args.port
    #if -p not specifed then scan default ports
else:
     ports_to_scan = range(1,1025)

#threading to handle faster scan
for p in ports_to_scan:
    t = threading.Thread(target=scan, args=(host,p))
    t.start()
    threads.append(t)

#wait for all threads
for t in threads:
    t.join()


open_ports.sort()

# Final report!!
if args.output is not None:
    with open(scan_output, 'w') as f:
              f.write("\n--------------\n")
              f.write("Scan Report\n")
              f.write(f"Target: {host}\n")
              f.write(f"Open ports: {', '.join(map(str, open_ports))}\n")
print("\n--------------")
print("Scan Report")
print(f"Target: {host}")
print(f"Open ports: {', '.join(map(str, open_ports))}\n")