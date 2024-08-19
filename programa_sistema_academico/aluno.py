#aluno.py:
from database import Database

class Aluno:
    def __init__(self, nome=None, data_nascimento=None, matricula=None, id_curso_fk=None, id_aluno=None):
        self.__id_aluno = id_aluno
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__matricula = matricula
        self.__id_curso_fk = id_curso_fk

    def adicionar_aluno(self, nome, data_nascimento, matricula, id_curso_fk):
        db = Database()
        db.conectar()
        query = '''INSERT INTO Alunos (nome, data_nascimento, matricula, id_curso_fk) 
                   VALUES (%s, %s, %s, %s)'''
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__matricula = matricula
        self.__id_curso_fk = id_curso_fk
        db.get_cursor().execute(query, (self.__nome, self.__data_nascimento, self.__matricula, self.__id_curso_fk))
        db.get_conexao().commit()
        db.get_cursor().close()
        db.get_conexao().close()
        return True


    @staticmethod
    def listar_alunos():
        db = Database()
        db.conectar()
        query = '''SELECT a.nome, a.data_nascimento, a.matricula, a.data_matricula, c.codigo, c.nome, c.carga_horaria 
        FROM Alunos AS a 
        INNER JOIN Cursos AS c ON a.id_curso_fk = c.id_curso'''
        db.get_cursor().execute(query)
        alunos = db.get_cursor().fetchall()
        db.get_cursor().close()
        db.get_conexao().close()
        return alunos

    def buscar_aluno_por_matricula(self, matricula):
        db = Database()
        db.conectar()
        query = '''SELECT a.nome, a.data_nascimento, a.matricula, a.data_matricula, c.codigo, c.nome, c.carga_horaria
        FROM Alunos AS a
        INNER JOIN Cursos AS c ON a.id_curso_fk = c.id_curso
        WHERE a.matricula = %s'''
        self.__matricula = matricula
        db.get_cursor().execute(query, (self.__matricula,))
        aluno = db.get_cursor().fetchone()
        db.get_cursor().close()
        db.get_conexao().close()
        return aluno

    def atualizar_aluno(self, novo_nome=None, nova_data_nascimento=None, nova_matricula=None, novo_id_curso_fk=None, matricula=None):
        db = Database()
        db.conectar()
        query = '''UPDATE Alunos 
                   SET nome = %s, data_nascimento = %s, matricula = %s, id_curso_fk = %s 
                   WHERE matricula = %s'''
        db.get_cursor().execute(query, (
            novo_nome or self.__nome, 
            nova_data_nascimento or self.__data_nascimento, 
            nova_matricula or self.__matricula, 
            novo_id_curso_fk or self.__id_curso_fk,
            matricula or self.__matricula
        ))
        db.get_conexao().commit()
        db.get_cursor().close()
        db.get_conexao().close()
        return True

    def deletar_aluno(self, matricula):
        db = Database()
        db.conectar()
        query = '''DELETE FROM Alunos WHERE matricula = %s'''
        self.__matricula = matricula
        db.get_cursor().execute(query, (self.__matricula,))
        db.get_conexao().commit()
        db.get_cursor().close()
        db.get_conexao().close()
        return True



