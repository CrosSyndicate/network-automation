#this will explore methods of configuring a vlan on the cisco test sandbox environment I found

#I would also like to roll back any changes before disconnecting

from netmiko import ConnectHandler
import pandas as pd
import csv
#found NAPALM module online - used for rolling back configuration changes - explore later
import napalm

#defining csv that has list of users - explore later
user_list = open('test_users.csv')

XR1 = {
    "device_type":"cisco_ios",
    "ip":"sandbox-iosxr-1.cisco.com",
    "username":"admin",
    "password":"C1sco12345"
}

#define CSV that contains userlist
user_list = open('test_users.csv')
user_list.readline()
csv_user_list = csv.reader(user_list)

# define the device
# enable EXEC mode
# send vlan configuration
# show vlans
net_connect = ConnectHandler(**XR1)
print(net_connect.find_prompt())
# output = net_connect.send_config_set(['vlan 10,20,30,40,50,60'])
output = net_connect.send_command('enable')
output = net_connect.send_command('reload')
output = net_connect.send_command('show vlan')
print(output)

net_connect.disconnect()