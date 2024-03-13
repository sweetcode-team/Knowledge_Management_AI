from dataclasses import dataclass

@dataclass
class ConfigurationOperationResponse:
    status: bool
    message: str
    
    def ok(self) -> bool:
        return self.status