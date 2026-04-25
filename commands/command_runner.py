import cmd
import readline
from device.base_device import DeviceInterface
from device.connector import Connector
from models.device_profile import DeviceProfile
from parser.parser import Parser
import logging

# logging settings
logging.basicConfig(
    filename='logs/device_tool.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

if not hasattr(readline, 'backend'):
    readline.backend = 'readline'

class CommandRunner( cmd.Cmd):
    prompt = '(main)>> '
    intro = 'Welcome! Type ? to list commands.\n'

    def __init__(self, device: DeviceInterface, connector: Connector, device_profile: DeviceProfile):
        super().__init__()
        self.device = device
        self.connector = connector
        self.device_profile = device_profile
    
    # For Android devices, checking if the device is still connected before executing any command
    def set_android_status(self):
        if self.device.device_type == "real" and self.device.isConnected:
            if not self.connector.is_device_connected():
                self.device.isConnected = False

    def do_connect(self, arg):
        'Connect to the device: connect'
        self.connector.connect(self.device)
        logging.info("User tried to connect to the device.")
    
    def do_connectionstatus(self, arg):
        'Check connection status: status'
        self.set_android_status()
        self.connector.isConnected(self.device)

    def do_disconnect(self, arg):
        'Disconnect from the device: disconnect'
        self.connector.disconnect(self.device)
        logging.info("User tried to disconnect from the device.")

    def do_checkbattery(self, arg):
        'Check battery level and status: checkbattery'
        self.set_android_status()
        result = self.device.execute_command("get_battery")
        # Handle empty result or error message
        if result == "":
            return
        elif result.startswith("Error occurred"):
            print(result)
            return
        
        if self.device.device_type == "mock":
         parsed = Parser.parse_mock_battery(result)
        else:
            parsed = Parser.parse_android_battery(result)
        print(f"Battery level: {parsed['battery_level']}, ({parsed['status']})")
        logging.info("User tried to check battery level.")

    def do_checkos(self,arg):
        'Check operating system and version: checkos'
        self.set_android_status()
        result = self.device.execute_command("get_os")

        if result == "":
            return
        elif result.startswith("Error occurred"):
            print(result)
            return
        
        parsed = Parser.parse_os(result)
        print(f"Operating system: {parsed['os']} {parsed['version']}")
        logging.info("User tried to check operating system information.")

    def do_checkmodel(self,arg):
        'Check device model and manufacturer: checkmodel'
        self.set_android_status()
        result = self.device.execute_command("get_model")

        if result == "":
            return
        elif result.startswith("Error occurred"):
            print(result)
            return
        
        parsed = Parser.parse_device_model(result)
        print(f"Device model: {parsed['manufacturer']} {parsed['model']}")
        logging.info("User tried to check device model information.")

    def do_showprofile(self, arg):
        'Show complete device profile: showprofile'
        self.set_android_status()
        self.device_profile.show_profile(self.device)
        
    def do_exit(self, arg):
        'Exit the command runner: exit'
        print('Exiting...')
        logging.info("user left device context.")
        return True
    
    def emptyline(self):
        pass


class CommandShell(cmd.Cmd):
    """The main shell that holds the list of devices."""
    intro = 'Welcome! Type ? to list commands.\n'
    prompt = ">> "

    def __init__(self, devices: dict, connector: Connector, device_profile: DeviceProfile):
        super().__init__()
        self.devices = devices # Dictionary of device_name: device_instance
        self.connector = connector
        self.device_profile = device_profile

    def do_list(self, arg):
        """List available devices."""
        print("Available devices:\n", "\n".join(self.devices.keys()))

    def do_select(self, device_name):
        """Select a device to manage it."""
        if device_name in self.devices:
            sub_shell = CommandRunner(self.devices[device_name], self.connector, self.device_profile)
            logging.info(f"User selected to connect to the {device_name} device.")
            sub_shell.cmdloop()
        else:
            print(f"Error: Device '{device_name}' not found. Use 'list'.")
            logging.warning(f"User attempted to select non-existent device: {device_name}")
    def do_exit(self, arg):
        """Exit the program."""
        logging.info("Session ended by user.")
        return True