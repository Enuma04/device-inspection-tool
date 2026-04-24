from device.mock_device import MockDevice
from device.connector import Connector
from models.device_profile import DeviceProfile
from commands.command_runner import CommandRunner

def main():
    connector = Connector()
    device = MockDevice()
    device_profile = DeviceProfile()
    command_runner = CommandRunner(device, connector, device_profile)
    command_runner.cmdloop()

if __name__ == "__main__":
    main()