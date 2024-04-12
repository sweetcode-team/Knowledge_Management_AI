"""
Modulo contenente le eccezioni personalizzate per l'API.
"""
class APIBadRequest(Exception):
    def __init__(self, message, status_code=None):
        self.message = message
        if status_code is None:
            self.status_code = 400
        else:
            self.status_code = status_code
"""
Eccezione per documento non supportato.
"""
class DocumentNotSupported(APIBadRequest):
    def __init__(self, message="Documento non supportato."):
        super().__init__(message, status_code=422)

"""
Eccezione per parametri insufficienti.
"""
class InsufficientParameters(APIBadRequest):
    def __init__(self, message="Parametri insufficienti o errati."):
        super().__init__(message, status_code=400)

"""
Eccezione per elaborazione API.
"""
class APIElaborationException(Exception):
    def __init__(self, message):
        self.message = message
        self.status_code = 500
        
class ConfigurationNotSetException(Exception):
    def __init__(self, message="Configurazione non impostata."):
        self.message = message
        self.status_code = 401