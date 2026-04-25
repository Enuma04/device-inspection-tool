import subprocess
from device.base_device import DeviceInterface

class Connector:
    def __init__(self):
        pass

    def is_device_connected(self):
        try:
            output = subprocess.check_output(['adb', 'devices']).decode('utf-8')
            lines = output.strip().split('\n')[1:]  
            devices = [line for line in lines if line.endswith('\tdevice')]
            return len(devices) > 0
        except subprocess.CalledProcessError:
             return False

    def connect(self, device: DeviceInterface):
        if not device.isConnected and device.device_type == "mock":
            print("Device connected successfully")
            device.isConnected = True
        elif device.isConnected and device.device_type == "mock":
            print("The device is already connected")
        elif device.device_type == "real":
            try:
                subprocess.check_output(['adb', "start-server"]).decode('utf-8')
                if self.is_device_connected():
                    device.isConnected = True
                    print("Device is connected")
                else:
                    print("Device not detected. Please ensure that ADB is installed and the usb cable is physically connected.")
            except subprocess.CalledProcessError:
                print("There was an error disconnecting the device.")

    def isConnected(self, device: DeviceInterface):
        print(f"Device connection status: {'Connected' if device.isConnected else 'Not Connected'}")
    
    def disconnect(self, device: DeviceInterface):
        if  device.device_type == "mock":
            device.isConnected = False
            print("Device is disconnected.")
        elif device.device_type == "real":
            try:
                subprocess.check_output(['adb', 'kill-server'], stderr=subprocess.STDOUT)
                device.isConnected = False
                print("Device is disconnected. Please physically disconnect the device from the computer.")
            except subprocess.CalledProcessError as e:
                error_msg = e.output.decode('utf-8')
                device.isConnected = False
                if "10061" in error_msg:
                    print("Please ensure your device is connected and ADB is enabled.")
                else:
                    print(f"There was an error disconnecting the device: {error_msg}")
