from netmiko import ConnectHandler
import os
import re
import getpass

username = input("Enter your username : ")
pswd = input("And your password : ")
device = {
          'ip':'10.56.80.7',
          'username':username,
          'password':pswd,
          'secret':'c0d312sw!',
          'device_type':'cisco_ios'
          }

print("-"*80)
connection = ConnectHandler(**device)

connection.enable()
host = connection.send_command('show running-config | include hostname')

gethost = re.split('\s',host)
hname = gethost[1]
filename = hname+'.txt'

output = connection.send_command("sh run")

with open(filename,'w') as f:
	f.write(output)

print("Backup completed for {}".format(hname))

print("-"*80)
