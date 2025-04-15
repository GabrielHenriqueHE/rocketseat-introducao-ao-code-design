class HttpUnprocessableEntityError(Exception):
    def __init__(self, message: str):
        self.message = message
        self.name = 'Unprocessable Entity'
        self.status_code = 422
        super().__init__(self.message)