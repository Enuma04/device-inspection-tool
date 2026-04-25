from device.base_device import DeviceInterface
import subprocess

class AndroidADBDevice(DeviceInterface) :
    def __init__(self):
        self.isConnected = False
        self.device_type = "real"
        self.COMMAND_MAP = {
            "get_battery": self.get_battery_info,
            "get_os": self.get_os_info,
            "get_model": self.get_model_info
        }

    def get_battery_info(self):
        try:
            result = subprocess.check_output(["adb", "shell", "dumpsys", "battery"]).decode("utf-8")
            return result
        except subprocess.CalledProcessError:
            return "Error occurred while fetching battery info."

    def get_os_info(self):
        try:
            result = subprocess.check_output(["adb", "shell", "getprop", "ro.build.version.release"]).decode("utf-8").strip()
            return f"Operating System: Android {result}"
        except subprocess.CalledProcessError:
            return "Error occurred while fetching OS info."

    def get_model_info(self):
        try:
            result = subprocess.check_output(["adb", "shell", "getprop", "ro.product.model"]).decode("utf-8").strip()
            manufacturer = subprocess.check_output(["adb", "shell", "getprop", "ro.product.manufacturer"]).decode("utf-8").strip()
            return f"Device Manufacturer: {manufacturer} and device model: {result}"
        except subprocess.CalledProcessError:
            return "Error occurred while fetching model info."

    def execute_command(self, command:str):
        if not self.isConnected:
            print("Device is not connected. Please connect to the device first.")
            return ""
        command_name = self.COMMAND_MAP.get(command, lambda: "Unknown command")
        return command_name()
