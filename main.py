from device.mock_device import MockDevice
from device.connector import Connector
from models.device_profile import DeviceProfile
from commands.command_runner import CommandShell
from device.android_adb_device import AndroidADBDevice

def main():
    connector = Connector()
    mock_device = MockDevice()
    device_profile = DeviceProfile()
    adb_device = AndroidADBDevice()
    device_list = {
        "mock": mock_device,
        "adb": adb_device
    }
    command_runner = CommandShell(device_list, connector, device_profile)
    command_runner.cmdloop()

if __name__ == "__main__":
    main()