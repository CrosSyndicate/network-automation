import os

from dotenv import load_dotenv
from netmiko import ConnectHandler

load_dotenv()

cisco = {
    "device_type": "cisco_ios",
    "host": "172.29.151.3",
    "username": os.getenv("LAB_USERNAME"),
    "password": os.getenv("LAB_PASSWORD"),
    "fast_cli": False,
}