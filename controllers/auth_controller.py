from models.user_model import UserModel
import bcrypt


class AuthController:
    def __init__(self) -> None:
        self.__user_model = UserModel()

    def authenticate(self, username, password):
        ''' Autentica o usuário verificando o username e a senha. '''
        user = self.__user_model.get_user_by_username(username)

        if user is None:
            return False
        
        stored_password = user[1]

        return bcrypt.checkpw(password.encode('utf-8'), stored_password)
    
    def create_new_user(self, username, password):
        ''' Cria um novo usuário com a senha hasheada. '''
        self.__user_model.create_user(username, password)
        return True
