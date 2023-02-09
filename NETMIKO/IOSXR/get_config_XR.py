#script to connect to CISCO XR sandbox and write config to a file named switch_running.txt

from netmiko import ConnectHandler

XR = {
    "device_type":"cisco_ios",
    "ip":"sandbox-iosxr-1.cisco.com",
    "username":"admin",
    "password":"C1sco12345"
}

net_connect = ConnectHandler(**XR)
print(net_connect.find_prompt())


output = net_connect.send_command('show running-config')
save_file = open("switch_running.txt","w")
save_file.write(output)
save_file.close()

#this prints what was written into the txt file
print(output)

net_connect.disconnect()