from dataclasses import dataclass
from domain.configuration.configuration_operation_response import ConfigurationOperationResponse

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
    
    """
    Returns a ConfigurationOperationResponse object with the same status and message.
    Returns:
        ConfigurationOperationResponse: The ConfigurationOperationResponse object.
    """
    def toConfigurationOperationResponse(self):
        return ConfigurationOperationResponse(self.ok(), self.message)