#curso.py:
from database import Database


class Curso:
    def __init__(self, codigo=None, nome=None, carga_horaria=None, id_curso=None):
        self.__id_curso = id_curso
        self.__codigo = codigo
        self.__nome = nome
        self.__carga_horaria = carga_horaria


    def buscar_id_curso_por_codigo(self, codigo):
        db = Database()
        db.conectar()
        query = '''SELECT id_curso FROM Cursos WHERE codigo = %s '''
        self.__codigo = codigo
        db.get_cursor().execute(query, (self.__codigo,))
        id_curso = db.get_cursor().fetchone()
        db.get_cursor().close()
        db.get_conexao().close()
        return id_curso
        

    def adicionar_curso(self, codigo, nome, carga_horaria):
        db = Database()
        db.conectar()
        query = '''INSERT INTO Cursos (codigo, nome, carga_horaria) VALUES (%s, %s, %s)'''
        self.__codigo = codigo
        self.__nome = nome
        self.__carga_horaria = carga_horaria
        db.get_cursor().execute(query, (self.__codigo, self.__nome, self.__carga_horaria))
        db.get_conexao().commit()
        db.get_cursor().close()
        db.get_conexao().close()
        return True

    @staticmethod
    def listar_cursos():
        db = Database()
        db.conectar()
        query = '''SELECT codigo, nome, carga_horaria FROM Cursos'''
        db.get_cursor().execute(query)
        cursos = db.get_cursor().fetchall()
        db.get_cursor().close()
        db.get_conexao().close()
        return cursos
  

    def buscar_curso_por_codigo(self, codigo):
        db = Database()
        db.conectar()
        query = '''SELECT codigo, nome, carga_horaria FROM Cursos WHERE codigo = %s'''
        self.__codigo = codigo
        db.get_cursor().execute(query, (self.__codigo,))
        curso = db.get_cursor().fetchone()
        db.get_cursor().close()
        db.get_conexao().close()
        return curso
    
    def buscar_alunos_por_curso(self, codigo):
        db = Database()
        db.conectar()
        query = '''SELECT a.nome, a.data_nascimento, a.matricula, a.data_matricula
        FROM Cursos AS c
        INNER JOIN Alunos AS a ON c.id_curso = a.id_curso_fk
        WHERE c.codigo = %s'''
        self.__codigo = codigo
        db.get_cursor().execute(query, (self.__codigo,))
        alunos = db.get_cursor().fetchall()
        db.get_cursor().close()
        db.get_conexao().close()
        return alunos
    

    def atualizar_curso(self, novo_codigo=None, novo_nome=None, nova_carga_horaria=None, codigo=None):
        db = Database()
        db.conectar()
        query = '''UPDATE Cursos 
                SET codigo = %s, nome = %s, carga_horaria = %s 
                WHERE codigo = %s'''
        db.get_cursor().execute(query, (novo_codigo or self.__codigo, novo_nome or self.__nome, nova_carga_horaria or self.__carga_horaria, codigo or self.__codigo))
        db.get_conexao().commit()
        db.get_cursor().close()
        db.get_conexao().close()
        return True

    def deletar_curso(self, codigo):
        db = Database()
        db.conectar()
        query = '''DELETE FROM Cursos WHERE codigo = %s'''
        self.__codigo = codigo
        db.get_cursor().execute(query, (self.__codigo,))
        db.get_conexao().commit()
        db.get_cursor().close()
        db.get_conexao().close()
        return True

    


