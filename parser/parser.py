from device.mock_device import MockDevice
import re

class Parser:
    def __init__(self):
        pass

    @staticmethod
    def parse_battery( arg: str):
        match = re.search(r"The battery level is (\d+) and the device is currently (\w+)", arg)
        if match:
            battery_level = int(match.group(1))
            status = match.group(2)
        else:
            battery_level = "unavailable"
            status = "unavailable"
        dict = {
            "battery_level": battery_level,
            "status": status
        }
        return dict
    
    @staticmethod
    def parse_os( arg: str):
        match = re.search(r"Operating System: (\w+) (\d+)", arg)
        if match:
            os = match.group(1)
            version = int(match.group(2))
        else:
            os = "unavailable"
            version = "unavailable"
        dict = {
            "os": os,
            "version": version
        }
        return dict
    
    @staticmethod
    def parse_device_model( arg: str):
        match = re.search(r"Device Manufacturer: (\w+) and device model:(.*)", arg)
        if match:
            model = match.group(2)
            manufacturer = match.group(1)
        else:
            model = "unavailable"
            manufacturer = "unavailable"
        dict = {
            "model": model,
            "manufacturer": manufacturer
        }
        return dict