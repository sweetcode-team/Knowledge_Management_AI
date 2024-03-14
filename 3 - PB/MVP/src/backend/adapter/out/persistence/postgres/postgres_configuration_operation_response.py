from dataclasses import dataclass

"""
This class is used to store the response of a configuration operation in Postgres.
"""
@dataclass
class PostgresConfigurationOperationResponse:
    status: bool
    message: str
    
    """
    Returns the status of the operation.
    Returns:
        bool: The status of the operation.
    """
    
    def ok(self) -> bool:
        return self.status