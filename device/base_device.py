from abc import ABC, abstractmethod
class DeviceInterface(ABC):
    @abstractmethod
    def execute_command(self, command: str) -> str:
        pass