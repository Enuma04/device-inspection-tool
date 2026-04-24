class MockDevice:
    def __init__(self):
        self.battery_level = 83
        self.status = "charging"
        self.os = "Android"
        self.version = 13
        self.model = "Pixel 6"
        self.manufacturer = "Google"
        self.isConnected = False

    def execute_command(self, command: str):
        if not self.isConnected:
            print("Device is not connected. Please connect to the device first.")
            return ""
        if command == "get_battery" :
           return f"The battery level is {self.battery_level} and the device is currently {self.status}"
        elif command == "get_os":
            return f"Operating System: {self.os} {self.version}"
        elif command == "get_model":
            return f"Device Manufacturer: {self.manufacturer} and device model:{self.model}"
        else:
            return "Unknown command"
