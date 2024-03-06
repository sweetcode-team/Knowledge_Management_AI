from dataclasses import dataclass

@dataclass
class ConfigurationResponse:
    def __init__(self, status: str, message: str):
        self.status = status
        self.message = message