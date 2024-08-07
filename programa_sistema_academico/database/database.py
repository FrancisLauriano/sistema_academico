## database/database.py:
import mysql.connector
from config.db_config import Config

class Database:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            database=Config.DB_NAME,
        )
        self.cursor = self.conexao.cursor()

    def criar_tabelas(self):
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS Cursos(
                    id_curso INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
                    codigo VARCHAR(10) NOT NULL UNIQUE,
                    nome VARCHAR(100) NOT NULL,
                    carga_horaria FLOAT NOT NULL
            )'''
        )

        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS Alunos(
                id_aluno INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
                nome VARCHAR(100) NOT NULL,
                data_nascimento DATE NOT NULL,
                matricula VARCHAR(10) NOT NULL UNIQUE,
                data_matricula TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                id_curso_fk INT NOT NULL,
                FOREIGN KEY (id_curso_fk) REFERENCES Cursos (id_curso)        
            )'''
        )
        
        self.conexao.commit()
        self.conexao.close()
