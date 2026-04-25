from device.mock_device import MockDevice
import re

class Parser:
    def __init__(self):
        pass

    @staticmethod
    def parse_mock_battery( arg: str):
        match = re.search(r"The battery level is (\d+) and the device is currently (\w+)", arg)
        if match:
            battery_level = int(match.group(1))
            status = match.group(2)
        else:
            battery_level = "unavailable"
            status = "unavailable"
        mock_battery_data = {
            "battery_level": battery_level,
            "status": status
        }
        return mock_battery_data

    @staticmethod
    def parse_os( arg: str):
        match = re.search(r"Operating System: (\w+) (\d+)", arg)
        if match:
            os = match.group(1)
            version = int(match.group(2))
        else:
            os = "unavailable"
            version = "unavailable"
        os_data = {
            "os": os,
            "version": version
        }
        return os_data
    
    @staticmethod
    def parse_device_model( arg: str):
        match = re.search(r"Device Manufacturer: (\w+) and device model:(.*)", arg)
        if match:
            model = match.group(2)
            manufacturer = match.group(1)
        else:
            model = "unavailable"
            manufacturer = "unavailable"
        model_data = {
            "model": model,
            "manufacturer": manufacturer
        }
        return model_data
    
    @staticmethod
    def parse_android_battery( arg: str):
        match = re.search(r"level: (\d+)", arg)
        status_match = re.search(r"status: (\d+)", arg)
        if match and status_match:
            battery_level = int(match.group(1))
            status = 'charging' if int(status_match.group(1)) == 2 else 'not charging'
        else:
            battery_level, status = "unavailable", "unavailable"
        android_battery_data = {
            "battery_level": battery_level,
            "status": status
        }
        return android_battery_data