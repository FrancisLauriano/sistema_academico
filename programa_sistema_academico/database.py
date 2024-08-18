#database.py:
from config import Config
import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        self.__host=Config.DB_HOST
        self.__port=Config.DB_PORT
        self.__user=Config.DB_USER
        self.__password=Config.DB_PASSWORD
        self.__database=Config.DB_DATABASE
        self.__conexao=None
        self.__cursor=None

    
    def conectar(self):
        try:
            self.__conexao = mysql.connector.connect(
                host=self.__host,
                port=self.__port,
                user=self.__user,
                password=self.__password,
                database=self.__database
            )
            self.__cursor = self.__conexao.cursor()
        except Error as err:
            self.__conexao = None
            self.__cursor = None
            print(f'Error starting database:\n{err}') 

    
    def get_cursor(self):
        return self.__cursor

    def get_conexao(self):
        return self.__conexao
        



        