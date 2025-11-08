
class UsuarioBuscar():
    def __init__(self, isSuccess, message , exists):
        self.isSuccess = isSuccess
        self.message = message
        self.exists = exists
    isSuccess : bool
    message: str
    exists: bool