import cmd
import readline
from device.mock_device import MockDevice
from device.connector import Connector
from models.device_profile import DeviceProfile
from parser.parser import Parser

if not hasattr(readline, 'backend'):
    readline.backend = 'readline'
    
class CommandRunner( cmd.Cmd):
    prompt = '>> '
    intro = 'Welcome! Type ? to list commands.\n'

    def __init__(self, device: MockDevice, connector: Connector, device_profile: DeviceProfile):
        super().__init__()
        self.device = device
        self.connector = connector
        self.device_profile = device_profile
    
    def do_connect(self, arg):
        'Connect to the device: connect'
        self.connector.connect(self.device)
    
    def do_connectionstatus(self, arg):
        'Check connection status: status'
        self.connector.isConnected(self.device)

    def do_disconnect(self, arg):
        'Disconnect from the device: disconnect'
        self.connector.disconnect(self.device)

    def do_checkbattery(self, arg):
        'Check battery level and status: checkbattery'
        result = self.device.execute_command("get_battery")
        parsed = Parser.parse_battery(result)
        print(f"Battery level: {parsed['battery_level']}, ({parsed['status']})")

    def do_checkos(self,arg):
        'Check operating system and version: checkos'
        result = self.device.execute_command("get_os")
        parsed = Parser.parse_os(result)
        print(f"Operating system: {parsed['os']} {parsed['version']}")

    def do_checkmodel(self,arg):
        'Check device model and manufacturer: checkmodel'
        result = self.device.execute_command("get_model")
        parsed = Parser.parse_device_model(result)
        print(f"Device model: {parsed['manufacturer']} {parsed['model']}")

    def do_showprofile(self, arg):
        'Show complete device profile: showprofile'
        self.device_profile.show_profile(self.device)
        
    def do_exit(self, arg):
        'Exit the command runner: exit'
        print('Exiting...')
        return True
    
    def emptyline(self):
        pass
