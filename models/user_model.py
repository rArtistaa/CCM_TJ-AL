from config import get_connection
import sqlite3
import bcrypt


class UserModel:
    def __init__(self) -> None:
        self.__connection = get_connection()

    def create_user(self, name, email, password):
        ''' Método público para criar usuarios. '''
        cursor = self.__connection.cursor()
        hashed_password = self.__hash_password(password)
        query = "INSERT INTO users (name, email, password) VALUES (?, ?, ?)"
        cursor.execute(query, (name, email, hashed_password))
        self.__connection.commit()
        cursor.close()
    
    def get_user_by_email(self, email):
        ''' Método público para buscar usuário. '''
        cursor = self.__connection.cursor()
        query = "SELECT name, password FROM users WHERE email = ?"
        cursor.execute(query, (email,))
        user = cursor.fetchone()
        cursor.close()
        return user
    
    def name_exists(self, name):
        ''' Busca um nome registrado no sistema. '''
        query = 'SELECT COUNT(*) FROM users where name = ?'
        cursor = self.__connection.cursor()
        cursor.execute(query, (name,))
        result = cursor.fetchone()
        cursor.close()
        return result[0] > 0
    
    def email_exists(self, email):
        ''' Busca um Email registrado no sistema '''
        query = 'SELECT COUNT(*) FROM users WHERE email = ?'
        cursor = self.__connection.cursor()
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        cursor.close()
        return result[0] > 0

    def __hash_password(self, password):
        ''' Método privado para hashear a senha. '''
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
