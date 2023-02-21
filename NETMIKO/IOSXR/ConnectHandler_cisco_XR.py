#Simple script to connect to CISCO XR sandbox and report back ip info

from netmiko import ConnectHandler

#define the device
XR = {
    "device_type":"cisco_ios",
    "ip":"sandbox-iosxr-1.cisco.com",
    "username":"admin",
    "password":"C1sco12345"
}

'''OLD-passing info in manually'''
#net_connect = ConnectHandler(device_type="cisco_ios",host="sandbox-iosxe-recomm-1.cisco.com",username="developer", password="C1sco12345")

net_connect = ConnectHandler(**XR)
#prints the current network device prompt
print(net_connect.find_prompt())


output = net_connect.send_command('sh ip int brief')
print(output)

net_connect.disconnect()

#print(CSR)