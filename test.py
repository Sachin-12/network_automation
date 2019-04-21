import paramiko
from netmiko import ConnectHandler
import time
import sys
from datetime import datetime
import warnings
warnings.filterwarnings(action='ignore',module='.*paramiko.*')
# ip = "10.131.18.1"
# username = "admin"
# password = "Tata@1234"
# selected_ip_file = open('ip_file.txt','r')
# ip_list = selected_ip_file.readlines()
# i=0
# selected_user_file = open('usr_file.txt', 'r')

def repeat():
    response = input("Continue : 'y' or 'n' :")
    if response == "n":
        sys.exit()
    ip = input("Enter IP: ")
    username = input("Enter username :")
    password = input("Enter password :")

    return ip,username,password

# Starting from the beginning of the file

# selected_user_file.seek(0)

# Reading the username from the file
# username = selected_user_file.readlines()[i].split(',')[0].rstrip("\n")
# print(username)

# Starting from the beginning of the file
# selected_user_file.seek(0)

# Reading the password from the file
# password = selected_user_file.readlines()[i].split(',')[1].rstrip("\n")
# print(password


while True:
    cred_list = repeat()
    print(cred_list)

    b = {
        "host": cred_list[0],
        "username": cred_list[1],
        "password": cred_list[2],
        "device_type": "hp_procurve"
    }

    a = ConnectHandler(**b)
    a.enable()
    a.find_prompt()
    c = " "
    # Writing each line in the file to the device
    # list_command = ["ssh admin@10.131.18.44","admin123"]
    c = c + a.send_command("show running-config")
    # c = c + a.send_config_set(list_command)
    # c = c + a.send_command("show running-config")


    time.sleep(2)
    dt = str(datetime.now())
    dt_split = dt.split(" ")
    # dt_split[1][:8].replace(":","-")
    backup_filename = cred_list[0] + " " + dt_split[0] + " " + dt_split[1][:8].replace(":", "-")

    backup_file = open(backup_filename, 'w')
    backup_file.write(c)
    backup_file.close()
    # # Closing the user file

    # Closing the command file

    print(c)

    a.disconnect()