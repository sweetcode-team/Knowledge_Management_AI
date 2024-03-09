from dataclasses import dataclass

@dataclass
class ConfigurationOperationResponse:
    def __init__(self, status: bool, message: str):
        self.status = status
        self.message = message