from device.base_device import DeviceInterface

class MockDevice(DeviceInterface):
    def __init__(self):
        self.battery_level = 83
        self.status = "charging"
        self.os = "Android"
        self.version = 13
        self.model = "Pixel 6"
        self.manufacturer = "Google"
        self.isConnected = False
        self.device_type = "mock"
        self.COMMAND_MAP = {
            "get_battery": self.get_battery_info,
            "get_os": self.get_os_info,
            "get_model": self.get_model_info
        }

    def get_battery_info(self):
        return f"The battery level is {self.battery_level} and the device is currently {self.status}"
    
    def get_os_info(self):
        return f"Operating System: {self.os} {self.version}"    
    
    def get_model_info(self):
        return f"Device Manufacturer: {self.manufacturer} and device model:{self.model}"    
    
    def execute_command(self, command: str):
        if not self.isConnected:
            print("Device is not connected. Please connect to the device first.")
            return ""
        command_name = self.COMMAND_MAP.get(command, lambda: "Unknown command")
        return command_name()