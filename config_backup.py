from netmiko import ConnectHandler
import os
import re
import getpass
import time

username = input("Enter your username : ")
pswd = input("And your password : ")
enpswd = input("Enter enable password : ")


def ssh_connect(ip, username, pswd, enpswd):
    device = {
              'ip':ip, 
            'username':username,
            'password':pswd,
            'secret':enpswd',
            'device_type':'cisco_ios'
             }


    #Establishing connection
    connection = ConnectHandler(**device)
    #Getting into enable mode
    connection.enable()
    # Getting device hostname
    host = connection.send_command('show running-config | include hostname')
    gethost = re.split('\s',host)
    hname = gethost[1]
    filename = hname+'.txt'
    #Storing running config output in a variable
    output = connection.send_command("sh run")
    #Saving output in a text file with filename as hostname of the devices
    with open(filename,'w') as f:
        f.write(output)
    print("\nBackup completed for {}".format(hname))
    connection.disconnect()
    


#provide IPs below as ['1.1.1.1','2.2.2.2','3.3.3.3']
ip_list = ['10.49.32.11','10.56.80.7']
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


	




