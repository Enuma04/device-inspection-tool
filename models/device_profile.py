from device.mock_device import MockDevice
from parser.parser import Parser

class DeviceProfile:
    def __init__(self):
        self.battery_level = None
        self.battery_status = None
        self.os = None
        self.version = None
        self.model = None
        self.manufacturer = None

    def show_profile(self, device: MockDevice):
        if not device.isConnected:
            print("Device is not connected. Please connect to the device first.")
            return
        battery = device.execute_command("get_battery")
        os = device.execute_command("get_os")
        model= device.execute_command("get_model")
        battery_info = Parser.parse_battery(battery)
        os_info = Parser.parse_os(os)
        model_info = Parser.parse_device_model(model)

        self.battery_level = battery_info["battery_level"]
        self.battery_status = battery_info["status"]
        self.os = os_info["os"]
        self.version = os_info["version"]
        self.model = model_info["model"]
        self.manufacturer = model_info["manufacturer"]

        print(f"Device Profile:")
        print(f"Battery Level: {self.battery_level}% ({self.battery_status})")
        print(f"Operating System: {self.os} {self.version}")
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Device Model: {self.model}")
        