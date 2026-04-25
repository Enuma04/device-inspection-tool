import json
from device.base_device import DeviceInterface
from parser.parser import Parser

class DeviceProfile:
    def __init__(self):
        self.battery_level = None
        self.battery_status = None
        self.os = None
        self.version = None
        self.model = None
        self.manufacturer = None
        self.merged_info = None

    def show_profile(self, device: DeviceInterface):
        if not device.isConnected:
            print("Device is not connected. Please connect to the device first.")
            return
        battery = device.execute_command("get_battery")
        os = device.execute_command("get_os")
        model= device.execute_command("get_model")
        if device.device_type == "mock":
            battery_info = Parser.parse_mock_battery(battery)
        else:
            battery_info = Parser.parse_android_battery(battery)
        os_info = Parser.parse_os(os)
        model_info = Parser.parse_device_model(model)

        merged_info = {**battery_info, **os_info, **model_info}
        self.battery_level = merged_info["battery_level"]
        self.battery_status = merged_info["status"]
        self.os = merged_info["os"]
        self.version = merged_info["version"]
        self.model = merged_info["model"]
        self.manufacturer = merged_info["manufacturer"]
        self.merged_info = merged_info

        print(f"Device Profile:")
        print(f"Battery Level: {self.battery_level}% ({self.battery_status})")
        print(f"Operating System: {self.os} {self.version}")
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Device Model: {self.model}")

    def export_profile(self):
        with open("logs/device_profile.json", "w") as f:
            json.dump(self.merged_info, f, indent=4)
        