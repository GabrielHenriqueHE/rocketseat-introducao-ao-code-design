class HttpBadRequestError(Exception):
    def __init__(self, message: str):
        self.message = message
        self.name = 'Bad Request'
        self.status_code = 400
        super().__init__(self.message)