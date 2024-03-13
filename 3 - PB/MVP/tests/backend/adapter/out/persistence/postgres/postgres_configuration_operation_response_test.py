from dataclasses import dataclass

@dataclass
class PostgresConfigurationOperationResponse:
    status: bool
    message: str