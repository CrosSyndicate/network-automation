#script to connect to CISCO sandbox and create a file containing sandbox configuration data

from netmiko import ConnectHandler

CSR = {
    "device_type":"cisco_ios",
    "ip":"sandbox-iosxe-recomm-1.cisco.com",
    "username":"developer",
    "password":"C1sco12345"
}


net_connect = ConnectHandler(**CSR)
print(net_connect.find_prompt())


output = net_connect.send_command('sh ip int brief')
print(output)

net_connect.disconnect()

#print(CSR)