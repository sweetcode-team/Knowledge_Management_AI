from dataclasses import dataclass

"""
ConfigurationOperationResponse: classe che rappresenta la risposta di un'operazione di configurazione
    Attributes:
        status (bool): Lo stato dell'operazione
        message (str): Il messaggio dell'operazione
"""
@dataclass
class ConfigurationOperationResponse:
    status: bool
    message: str
    
    def ok(self) -> bool:
        return self.status