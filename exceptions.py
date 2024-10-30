# Exceções personalizadas

class RouteNotFoundError(Exception):
    ''' Exceção personalizada para rotas não encontradas. '''

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


