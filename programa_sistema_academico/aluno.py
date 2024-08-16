#código considerando uma pasta config e uma databese
#Caso ficar só com o arquivo config vou fazer os ajustes necessários

from database import Database

class Aluno:
    def __init__(self, nome=None, data_nascimento=None, matricula=None, id_curso_fk=None, id_aluno=None):
        self.__id_aluno = id_aluno
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__matricula = matricula
        self.__id_curso_fk = id_curso_fk

    def adicionar_aluno(self):
        db = Database()
        db.conectar()
        query = '''INSERT INTO Alunos (nome, data_nascimento, matricula, id_curso_fk) 
                   VALUES (%s, %s, %s, %s)'''
        db.get_cursor().execute(query, (self.__nome, self.__data_nascimento, self.__matricula, self.__id_curso_fk))
        db.get_conexao().commit()
        db.get_cursor().close()
        db.get_conexao().close()
        return True

    @staticmethod
    def listar_alunos():
        db = Database()
        db.conectar()
        query = '''SELECT * FROM Alunos'''
        db.get_cursor().execute(query)
        alunos = db.get_cursor().fetchall()
        db.get_cursor().close()
        db.get_conexao().close()
        return alunos

    def buscar_aluno(self):
        db = Database()
        db.conectar()
        query = '''SELECT * FROM Alunos WHERE matricula = %s'''
        db.get_cursor().execute(query, (self.__matricula,))
        aluno = db.get_cursor().fetchone()
        db.get_cursor().close()
        db.get_conexao().close()
        return aluno

    def atualizar_aluno(self, novo_nome=None, nova_data_nascimento=None, nova_matricula=None, novo_id_curso_fk=None):
        db = Database()
        db.conectar()
        query = '''UPDATE Alunos 
                   SET nome = %s, data_nascimento = %s, matricula = %s, id_curso_fk = %s 
                   WHERE id_aluno = %s OR matricula = %s'''
        db.get_cursor().execute(query, (
            novo_nome or self.__nome, 
            nova_data_nascimento or self.__data_nascimento, 
            nova_matricula or self.__matricula, 
            novo_id_curso_fk or self.__id_curso_fk,
            self.__matricula
        ))
        db.get_conexao().commit()
        db.get_cursor().close()
        db.get_conexao().close()
        return True

    def deletar_aluno(self):
        db = Database()
        db.conectar()
        query = '''DELETE FROM Alunos WHERE matricula = %s'''
        db.get_cursor().execute(query, (self.__id_aluno, self.__matricula))
        db.get_conexao().commit()
        db.get_cursor().close()
        db.get_conexao().close()
        return True


