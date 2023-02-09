#script to connect to CISCO XR sandbox, check if device is in config mode, if it isn't, then set config mode, then revert

from netmiko import ConnectHandler

XR = {
    "device_type":"cisco_ios",
    "ip":"sandbox-iosxr-1.cisco.com",
    "username":"admin",
    "password":"C1sco12345"
}

net_connect = ConnectHandler(**XR)

config = net_connect.check_config_mode()

print(net_connect.find_prompt())

net_connect.config_mode()

def check_config(net_connect, config):
    if config != True:
        print("Setting config mode")
        net_connect.config_mode()
        print(net_connect.check_config_mode())
    else:
        print("Device is already in config mode.")
        return


check_config(net_connect, config)

# output = net_connect.send_config_from_file("switch_running.txt")
# print(output)

#exit config mode and disconnects
net_connect.exit_config_mode()
#just making sure it's exiting config mode
print(config)
net_connect.disconnect()


### GRAVEYARD ###

# checks for config mode - if not in config mode, enters config mode, then exits config mode

# def check_config(net_connect):
#     print("Checking config mode")
#     net_connect.check_config_mode()
#     return

# def set_config(net_connect):
#     print("Checking config mode")
#     config = net_connect.check_config_mode()
#     while config == True:
#         print("IOS in config mode. Applying configuration.")
#         net_connect.send_config_from_file("switch_running.txt")
#     if config != True:
#         net_connect.config_mode
#     return