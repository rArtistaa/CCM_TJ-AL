from config import get_connection
import bcrypt


class UserModel:
    def __init__(self) -> None:
        self.__connection = get_connection()

    def create_user(self, username, password):
        ''' Método público para criar usuarios. '''
        cursor = self.__connection.cursor()
        hashed_password = self.__hash__password(password)
        query = "INSERT INTO users (username, password) VALUES (?, ?)"
        cursor.execute(query, (username, hashed_password))
        self.__connection.commit()
        cursor.close()
    
    def get_user_by_username(self, username):
        ''' Método público para buscar usuário. '''
        cursor = self.__connection.cursor()
        query = "SELECT username, password FROM user WHERE username = ?"
        cursor.execute(query, (username,))
        user = cursor.fetchone
        cursor.close()
        return user
    
    def __hash_password(self, password):
        ''' Método privado para hashear a senha. '''
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
