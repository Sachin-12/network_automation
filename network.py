# Importing the necessary modules
import sys
import os
# from netmiko import Netmiko,ConnectHandler,ssh_exception
from ip_file_valid import ip_file_valid
from ip_addr_valid import ip_addr_valid
from ip_reach import ip_reach
from netmiko_connect import ssh_connection,repeat_ssh_connection
# from datetime import datetime
# import time
from create_threads import create_threads

# Saving the list of IP addresses in ip.txt to a variable
ip_list = ip_file_valid()

# Verifying the validity of each IP address in the list
try:
    ip_addr_valid(ip_list)

except KeyboardInterrupt:
    print("\n\n* Program aborted by user. Exiting...\n")
    sys.exit()

# Verifying the reachability of each IP address in the list
try:
    ip_reach(ip_list)

except KeyboardInterrupt:
    print("\n\n* Program aborted by user. Exiting...\n")
    sys.exit()
# Calling threads creation function for one or multiple SSH connections
create_threads(ssh_connection,ip_list)
# End of program