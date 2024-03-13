class APIBadRequest(Exception):
    def __init__(self, message, status_code=None):
        self.message = message
        if status_code is None:
            self.status_code = 400
        else:
            self.status_code = status_code

class DocumentNotSupported(APIBadRequest):
    def __init__(self, message="Documento non supportato."):
        super().__init__(message, status_code=422)

class InsufficientParameters(APIBadRequest):
    def __init__(self, message="Parametri insufficienti o errati."):
        super().__init__(message, status_code=400)

class APIElaborationException(Exception):
    def __init__(self, message):
        self.message = message
        self.status_code = 500