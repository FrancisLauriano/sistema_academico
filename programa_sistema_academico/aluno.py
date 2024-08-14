#código considerando uma pasta config e uma databese
#Caso ficar só com o arquivo config vou fazer os ajustes necessários

from database.database import Database

class Aluno:
    def __init__(self, nome=None, data_nascimento=None, matricula=None, id_curso_fk=None, id_aluno=None):
        self.__id_aluno = id_aluno
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__matricula = matricula
        self.__id_curso_fk = id_curso_fk

    def adicionar_aluno(self):
        db = Database()
        query = '''INSERT INTO Alunos (nome, data_nascimento, matricula, id_curso_fk) 
                   VALUES (%s, %s, %s, %s)'''
        db.cursor.execute(query, (self.__nome, self.__data_nascimento, self.__matricula, self.__id_curso_fk))
        db.conexao.commit()
        db.cursor.close()
        db.conexao.close()
        return True

    @staticmethod
    def listar_alunos():
        db = Database()
        query = '''SELECT * FROM Alunos'''
        db.cursor.execute(query)
        alunos = db.cursor.fetchall()
        db.cursor.close()
        db.conexao.close()
        return alunos

    def buscar_aluno(self, identificador):
        db = Database()
        if isinstance(identificador, int):
            query = '''SELECT * FROM Alunos WHERE id_aluno = %s'''
            db.cursor.execute(query, (identificador,))
        else:
            query = '''SELECT * FROM Alunos WHERE matricula = %s'''
            db.cursor.execute(query, (identificador,))
        aluno = db.cursor.fetchone()
        db.cursor.close()
        db.conexao.close()
        return aluno

    def atualizar_aluno(self, novo_nome=None, nova_data_nascimento=None, nova_matricula=None, novo_id_curso_fk=None):
        db = Database()
        query = '''UPDATE Alunos 
                   SET nome = %s, data_nascimento = %s, matricula = %s, id_curso_fk = %s 
                   WHERE id_aluno = %s OR matricula = %s'''
        db.cursor.execute(query, (
            novo_nome or self.__nome, 
            nova_data_nascimento or self.__data_nascimento, 
            nova_matricula or self.__matricula, 
            novo_id_curso_fk or self.__id_curso_fk,
            self.__id_aluno,
            self.__matricula
        ))
        db.conexao.commit()
        db.cursor.close()
        db.conexao.close()
        return True

    def deletar_aluno(self):
        db = Database()
        query = '''DELETE FROM Alunos WHERE id_aluno = %s OR matricula = %s'''
        db.cursor.execute(query, (self.__id_aluno, self.__matricula))
        db.conexao.commit()
        db.cursor.close()
        db.conexao.close()
        return True
