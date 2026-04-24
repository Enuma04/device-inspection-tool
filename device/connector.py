from device.mock_device import MockDevice

class Connector:
    def __init__(self):
        pass

    def connect(self, device: MockDevice):
        if not device.isConnected:
            print("Device connected successfully")
            device.isConnected = True
        else:
            print("The device is already connected")

    def isConnected(self, device: MockDevice):
        print(f"Device connection status: {'Connected' if device.isConnected else 'Not Connected'}")
    
    def disconnect(self, device: MockDevice):
        if device.isConnected:
            device.isConnected = False
            print("Device disconnected.")
        else:
            print("The device is not connected")