
class UsuarioBuscar():
    def __init__(self, isSuccess, message , exists , id):
        self.isSuccess = isSuccess
        self.message = message
        self.exists = exists
        self.id = id
    isSuccess : bool
    message: str
    exists: bool
    id: int