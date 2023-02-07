#Simple script to connect to CISCO sandbox and report back ip info

from netmiko import ConnectHandler

CSR = {
    "device_type":"cisco_ios",
    "ip":"sandbox-iosxe-recomm-1.cisco.com",
    "username":"developer",
    "password":"C1sco12345"
}

'''OLD-passing info in manually'''
#net_connect = ConnectHandler(device_type="cisco_ios",host="sandbox-iosxe-recomm-1.cisco.com",username="developer", password="C1sco12345")

net_connect = ConnectHandler(**CSR)
print(net_connect.find_prompt())


output = net_connect.send_command('sh ip int brief')
print(output)

net_connect.disconnect()

#print(CSR)