from dataclasses import dataclass

@dataclass
class PostgresConfigurationOperationResponse:
    status: bool
    message: str
    
    def ok(self) -> bool:
        return self.status