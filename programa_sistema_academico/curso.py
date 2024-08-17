from config import Config
from database import Database

class Curso:
    def __init__(self, codigo=None, nome=None, carga_horaria=None, id_curso=None):
        self.__id_curso = id_curso
        self.__codigo = codigo
        self.__nome = nome
        self.__carga_horaria = carga_horaria

    def adicionar_curso(self):
        db = Database()
        db.conectar()
        query = '''INSERT INTO Cursos (codigo, nome, carga_horaria) 
                   VALUES (%s, %s, %s)'''
        db.get_cursor().execute(query, (self.__codigo, self.__nome, self.__carga_horaria))
        db.get_conexao().commit()
        db.get_cursor().close()
        db.get_conexao().close()
        return True

    @staticmethod
    def listar_cursos():
        db = Database()
        db.conectar()
        query = '''SELECT * FROM Cursos'''
        db.get_cursor().execute(query)
        cursos = db.get_cursor().fetchall()
        db.get_cursor().close()
        db.get_conexao().close()
        return cursos

    def buscar_curso(self):
        db = Database()
        db.conectar()
        query = '''SELECT * FROM Cursos WHERE codigo = %s'''
        db.get_cursor().execute(query, (self.__codigo,))
        curso = db.get_cursor().fetchone()
        db.get_cursor().close()
        db.get_conexao().close()
        return curso

    def atualizar_curso(self):
        db = Database()
        db.conectar()
        query = '''UPDATE Cursos 
                   SET nome = %s, carga_horaria = %s 
                   WHERE codigo = %s'''
        db.get_cursor().execute(query, (self.__nome, self.__carga_horaria, self.__codigo))
        db.get_conexao().commit()
        db.get_cursor().close()
        db.get_conexao().close()
        return True

    def deletar_curso(self):
        db = Database()
        db.conectar()
        query = '''DELETE FROM Cursos WHERE codigo = %s'''
        db.get_cursor().execute(query, (self.__codigo,))
        db.get_conexao().commit()
        db.get_cursor().close()
        db.get_conexao().close()
        return True

    ## construtor --> os atributos são privados
    # def __init__():

    ## metodo privado para conectar com banco de dados
    # def __conectar(self):

    ## metodo para adicionar curso
    # def adicionar_curso(self):

    ## metodo para listar todos os cursos
    # def listar_cursos():

    ## metodo para buscar o curso pelo código do curso
    ## buscar_curso(self):

    ## metodo para atualizar dados do curso
    ## def atualizar_curso(self):

    ## metodo para deletar o curso
    ## def deletar_curso(self):

