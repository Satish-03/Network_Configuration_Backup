from netmiko import ConnectHandler
from netmiko.ssh_exception import AuthenticationException
from netmiko.ssh_exception import NetMikoTimeoutException
import os
import os.path
import re
import getpass
import time
import sys


print("-"*80)
cmd_file = input("Enter path for operational mode commands : ")

if os.path.isfile(cmd_file) is True:
        with open(cmd_file, 'r') as f:
            cmd = f.readlines()
else:
    print("\nOops....Invalid path input....Please try again!")
    sys.exit()

        
print("-"*80)
username = input("Enter your username : ")
pswd = getpass.getpass("And your password : ")
enpswd = input("Enter enable password : ")


def ssh_connect(ip, username, pswd, enpswd):

    try:

        device = {
              'ip':ip, 
            'username':username,
            'password':pswd,
            'secret':enpswd,
            'device_type':'cisco_ios'
                  }
        
        #Establishing connection
        connection = ConnectHandler(**device)
        #Getting into enable mode
        connection.enable()
        # Getting device hostname
        host = connection.find_prompt()
        hname = host.strip('#')
        filename = hname+'.txt'
        #Storing running config output in a variable
        for each_cmd in cmd:
            output = connection.send_command(each_cmd.strip('\n'))
            with open(filename,'a') as f:
                f.write(output)
        print("Reading the running config")
        #output = connection.send_command("sh run")
        #Saving output in a text file with filename as hostname of the devices
        print("\nBackup completed for {}".format(hname))
        connection.disconnect()

    except (AuthenticationException):
       print("\nOops! Authentication fails    Try again....")
    except (NetMikoTimeoutException):
       print("\nSession timed out....Try again")
    

#provide IPs below as ['1.1.1.1','2.2.2.2','3.3.3.3']
ip_list = [
    
'10.74.0.3'

          ]

#Starting couting secs
start = time.time()

for ip in ip_list:
    print("-"*80)
    print("Getting in {}".format(ip))
    ssh_connect(ip, username, pswd, enpswd)
    
stop = time.time()
consume = stop - start

print("-"*80)
print("Activity is completed in {} secs".format(consume))
print("-"*80)


	




