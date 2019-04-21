import os.path
from netmiko import Netmiko,ConnectHandler,ssh_exception
import time
import warnings
import sys
import re
from datetime import datetime
warnings.filterwarnings(action="ignore", module=".*paramiko.*")
device={}

user_file = input("\n# Enter user file path and name ")
# Verifying the validity of the USERNAME/PASSWORD file
if os.path.isfile(user_file) == True:
    print("\n* Username/password file is valid :)\n")

else:
    print("\n* File {} does not exist :( Please check and try again.\n".format(user_file))
    sys.exit()

cmd_file = input("\n Enter command file path and name")
# Verifying the validity of the COMMANDS FILE
if os.path.isfile(cmd_file) == True:
    print("\n* Command file is valid :)\n")

else:
    print("\n* File {} does not exist :( Please check and try again.\n".format(cmd_file))
    sys.exit()
# Checking username/password file
# Prompting user for input - USERNAME/PASSWORD FILE
# Open SSHv2 connection to the device
def ssh_connection(ip,i):
    global user_file
    global cmd_file
    global device
    output=""
    from datetime import datetime
    # Creating SSH CONNECTION
    # Define SSH parameters
    try:
        selected_user_file = open(user_file, 'r')

        # Starting from the beginning of the file
        selected_user_file.seek(0)

        # Reading the username from the file
        username = selected_user_file.read().splitlines()[i].split(',')[0]
        print(username)

        # Starting from the beginning of the file
        selected_user_file.seek(0)

        # Reading the password from the file
        password = selected_user_file.read().splitlines()[i].split(',')[1]
        print(password)


        device = {
            "host" : ip,
            "username" : username,
            "password" : password,
            "device_type" : "hp_procurve",
        }
        connection = ConnectHandler(**device)
        selected_cmd_file= open('cmd_file.txt','r')
        commands = selected_cmd_file.read().splitlines()
        for command in commands:
            output = output + connection.send_config_set(command)
            time.sleep(2)
        selected_user_file.close()
        selected_cmd_file.close()
        dt = str(datetime.now())
        dt_split = dt.split(" ")
        # dt_split[1][:8].replace(":","-")
        backup_filename = ip + " " + dt_split[0] + " " + dt_split[1][:8].replace(":", "-")

        backup_file = open(backup_filename, 'w')
        backup_file.write(output)
        backup_file.close()
    except ssh_exception.NetMikoAuthenticationException:
        print("Authentication Error for {}. Please check the user file".format(ip))
    except ssh_exception.NetMikoTimeoutException:
        print("Timeout for {}. Please try again".format(ip))
    except ValueError:
        repeat_ssh_connection(ip,i)

def repeat_ssh_connection(ip,i):
    global user_file
    global cmd_file
    global device
    output = ""
    from datetime import datetime
    # Creating SSH CONNECTION
    # Define SSH parameters
    try:
        selected_user_file = open(user_file, 'r')

        # Starting from the beginning of the file
        selected_user_file.seek(0)

        # Reading the username from the file
        username = selected_user_file.read().splitlines()[i].split(',')[0]
        print(username)

        # Starting from the beginning of the file
        selected_user_file.seek(0)

        # Reading the password from the file
        password = selected_user_file.read().splitlines()[i].split(',')[1]
        print(password)

        device = {
            "host": ip,
            "username": username,
            "password": password,
            "device_type": "aruba_os",
        }
        connection = ConnectHandler(**device)
        selected_cmd_file = open('cmd_file.txt', 'r')
        commands = selected_cmd_file.read().splitlines()
        for command in commands:
            output = output + connection.send_command(command)
            time.sleep(2)
        selected_user_file.close()
        selected_cmd_file.close()
        dt = str(datetime.now())
        dt_split = dt.split(" ")
        # dt_split[1][:8].replace(":","-")
        backup_filename = ip + " " + dt_split[0] + " " + dt_split[1][:8].replace(":", "-")

        backup_file = open(backup_filename, 'w')
        backup_file.write(output)
        backup_file.close()
    except ssh_exception.NetMikoAuthenticationException:
        print("Authentication Error for {}. Please check the user file".format(ip))
    except ssh_exception.NetMikoTimeoutException:
        print("Timeout for {}. Please try again".format(ip))