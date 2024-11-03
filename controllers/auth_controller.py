from models.user_model import UserModel
import bcrypt


class AuthController:
    def __init__(self) -> None:
        self.__user_model = UserModel()

    def authenticate(self, email, password):
        ''' Autentica o usuário verificando o email e a senha. '''
        user = self.__user_model.get_user_by_email(email)

        if user is None:
            return False
        
        stored_password = user[1]

        return bcrypt.checkpw(password.encode('utf-8'), stored_password)
    
    def email_exists(self, email):
        return self.__user_model.email_exists(email)

    def create_new_user(self, name, email, password):
        ''' Cria um novo usuário com a senha hasheada. '''
        if self.email_exists(email):
            return False  
        self.__user_model.create_user(name, email, password)
        return True
