from dataclasses import dataclass

@dataclass
class ConfigurationOperationResponse:
    status: bool
    message: str