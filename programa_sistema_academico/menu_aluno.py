# menu_aluno.py:
from aluno import Aluno
from curso import Curso
from utils import limpar_terminal, pausar_execucao
import datetime

class MenuAluno:
    def __init__(self):
        self.aluno = Aluno()
        self.curso = Curso()

    def exibir_menu(self):
        while True:
            limpar_terminal()
            print('\n########## MENU ALUNO ##########\n')
            print('[1] Adicionar Aluno')
            print('[2] Listar Alunos')
            print('[3] Buscar Aluno por matrícula')
            print('[4] Atualizar Aluno')
            print('[5] Deletar Aluno')
            print('[6] Voltar')
            print('\n################################')

            try:
                opccao = int(input('OPÇÃO: '))

                if opccao == 1:
                    self.adicionar_aluno()
                elif opccao == 2:
                    self.listar_alunos()
                elif opccao == 3:
                    self.buscar_aluno()
                elif opccao == 4:
                    self.atualizar_aluno()
                elif opccao == 5:  
                    self.deletar_aluno()
                elif opccao == 6:
                    break
                else:
                    print(f'\n---------------')
                    print(f'Opção Inválida!')
                    print(f'---------------')                
            except ValueError:    
                print(f'\n-----------------------------------------') 
                print(f'Oops! Um erro ocorreu. Tente novamente...')   
                print(f'-----------------------------------------')  

    def adicionar_aluno(self):
        limpar_terminal()
        print('\n----------------- CADASTRO DE ALUNO -----------------\n')
        try:
            nome = input('Nome: ').strip().lower()
            data_nascimento = input('Data de Nascimento (YYYY-MM-DD): ').strip().lower()
            matricula = input('Matrícula (CPF - 11 digitos): ').strip().lower()
            codigo_curso = input('Código do Curso: ').strip().lower()

            #validação de nome
            if not nome or not isinstance(nome, str):
                print(f'\n--------------')
                print(f'Nome inválido.')
                print(f'--------------')
                pausar_execucao()
                return

            # validação de data de nascimento
            if not data_nascimento:
                print(f'\n----------------------------')
                print(f'Data de nascimento inválida.')
                print(f'----------------------------')
                pausar_execucao()
                return

            # validação de data de nascimento
            try:
                datetime.datetime.strptime(data_nascimento, '%Y-%m-%d')
            except ValueError:
                print(f'\n------------------------------------------------------') 
                print(f'Data de nascimento inválida. Use o formato YYYY-MM-DD.')
                print(f'------------------------------------------------------') 
                pausar_execucao()
                return

            # validação da matrícula (CPF)
            if not matricula or not matricula.isdigit() or len(matricula) != 11:
                    print(f'\n----------------------------------------------------')   
                    print(f'Matricula inválida. Deve conter 11 dígitos numéricos')
                    print(f'----------------------------------------------------') 
                    pausar_execucao()
                    return  

            # validação de código de curso
            if not codigo_curso or not isinstance(codigo_curso, str):
                print(f'\n-------------------------') 
                print(f'Código do curso inválido.')
                print(f'-------------------------') 
                pausar_execucao()
                return

            #verifica qual o id_curso correspondente ao codigo_curso
            id_curso_fk = self.curso.buscar_id_curso_por_codigo(codigo=codigo_curso)
            if id_curso_fk is not None and isinstance(id_curso_fk, tuple):
                id_curso_fk = id_curso_fk[0]

            if id_curso_fk is None:
                print(f'\n---------------------')
                print(f'Curso não encontrado.')
                print(f'---------------------')
                pausar_execucao()
                return
            
            # verifica se já existe cadsatro no sistema com a mesma matricula(CPF)

            if self.aluno.buscar_aluno_por_matricula(matricula=matricula):
                print(f'\n-----------------------------------------------') 
                print(f'Número de matrícula (CPF) já consta no sistema!')
                print(f'-----------------------------------------------') 
                pausar_execucao()
                return
            else:
                self.aluno.adicionar_aluno(nome=nome, data_nascimento=data_nascimento, matricula=matricula, id_curso_fk=id_curso_fk)
                print(f'\n-----------------------------') 
                print(f'Aluno cadastrado com sucesso!')
                print(f'-----------------------------') 
                pausar_execucao()
        except ValueError:   
            print(f'\n-----------------------------------------') 
            print(f'Oops! Um erro ocorreu. Tente novamente...')   
            print(f'-----------------------------------------') 
            pausar_execucao()


    def listar_alunos(self):
        limpar_terminal()

        largura_total = 220
        largura_nome = 60
        largura_DN = 20
        largura_matricula = 20
        largura_data_matricula = 20
        largura_codigo_curso = 20
        largura_nome_curso = 40
        largura_ch_curso = 20

        alunos = self.aluno.listar_alunos()
        if alunos is not None:
            print(f'\nRESULTADO:')
            print('-'*largura_total)
            print(f'{"NOME":<{largura_nome}} | {"DATA NASC":<{largura_DN}} | {"MATRÍCULA(CPF)":<{largura_matricula}} | {"DATA MATRÍCULA":<{largura_data_matricula}} | {"COD. CURSO":<{largura_codigo_curso}} | {"CURSO":<{largura_nome_curso}} | {"CH CURSO":<{largura_ch_curso}}')
            print('-'*largura_total)

            for aluno in alunos:
                nome = aluno[0]
                dataNasc = aluno[1].strftime('%d/%m/%Y')
                matricula = f'{aluno[2][:3]}.{aluno[2][3:6]}.{aluno[2][6:9]}-{aluno[2][9:]}'
                dataMatricula = aluno[3].strftime('%d/%m/%Y')
                codigo_curso = aluno[4]
                nome_curso = aluno[5]
                ch_curso = f'{aluno[6]:.1f}'

                print(f'{nome:<{largura_nome}} | {dataNasc:<{largura_DN}} | {matricula:<{largura_matricula}} | {dataMatricula:<{largura_data_matricula}} | {codigo_curso:<{largura_codigo_curso}} | {nome_curso:<{largura_nome_curso}} | {ch_curso:<{largura_ch_curso}}')
                print('-'*largura_total)
            pausar_execucao()
        else:
            print(f'\n-----------------------')  
            print(f'Nenhum aluno encontrado')
            print(f'-----------------------')  
            pausar_execucao() 
            return None 

    def view_aluno(self):
        largura_total = 220
        largura_nome = 60
        largura_DN = 20
        largura_matricula = 20
        largura_data_matricula = 20
        largura_codigo_curso = 20
        largura_nome_curso = 40
        largura_ch_curso = 20

        matricula = input('Informe o matrícula (CPF) do aluno: ').strip().lower()

        aluno = self.aluno.buscar_aluno_por_matricula(matricula=matricula)
        if aluno is not None:
            print(f'\nRESULTADO:')
            print('-'*largura_total)
            print(f'{"NOME":<{largura_nome}} | {"DATA NASC":<{largura_DN}} | {"MATRÍCULA(CPF)":<{largura_matricula}} | {"DATA MATRÍCULA":<{largura_data_matricula}} | {"COD. CURSO":<{largura_codigo_curso}} | {"CURSO":<{largura_nome_curso}} | {"CH CURSO":<{largura_ch_curso}}')
            print('-'*largura_total)

            nome = aluno[0]
            dataNasc = aluno[1].strftime('%d/%m/%Y')
            matricula = f'{aluno[2][:3]}.{aluno[2][3:6]}.{aluno[2][6:9]}-{aluno[2][9:]}'
            dataMatricula = aluno[3].strftime('%d/%m/%Y')
            codigo_curso = aluno[4]
            nome_curso = aluno[5]
            ch_curso = f'{aluno[6]:.1f}'

            print(f'{nome:<{largura_nome}} | {dataNasc:<{largura_DN}} | {matricula:<{largura_matricula}} | {dataMatricula:<{largura_data_matricula}} | {codigo_curso:<{largura_codigo_curso}} | {nome_curso:<{largura_nome_curso}} | {ch_curso:<{largura_ch_curso}}')
            print('-'*largura_total)
            return aluno
        else:
            return None    
           

    def buscar_aluno(self):
        limpar_terminal()
        print('\n----------------- LOCALIZAR ALUNO -----------------\n')
        
        localizar_aluno = self.view_aluno()

        if localizar_aluno is not None:
            pausar_execucao()
            return localizar_aluno
        else:
            print(f'\n-----------------------')
            print(f'Nenhum aluno encontrado')
            print(f'-----------------------')
            pausar_execucao()  
            return None

    def atualizar_aluno(self):
        limpar_terminal()
        print('\n----------------- ATUALIZAR ALUNO -----------------\n')

        aluno_encontrado = self.view_aluno()

        if aluno_encontrado is not None:

            print('\nDeseja atualizar aluno?')
            print('[1] Sim')
            print('[0] Não')
            try:
                continuar = int(input('OPÇÃO: '))

                if continuar == 0:
                    True
                elif continuar == 1:
                    limpar_terminal()
                    print('\n------------------------ ATUALIZAR ALUNO ------------------------\n')
                    try:
                        nome = input('Nome (ou clique ENTER para não alterar): ').strip().lower()
                        data_nascimento = input('Data de Nascimento (YYYY-MM-DD) (ou clique ENTER para não alterar): ').strip().lower()
                        nova_matricula = input('Matrícula (CPF - 11 digitos) (ou clique ENTER para não alterar): ').strip().lower()
                        codigo_curso = input('Código do Curso (ou clique ENTER para não alterar): ').strip().lower()

                        nome = nome if nome else aluno_encontrado[0]
                        data_nascimento = data_nascimento if data_nascimento else aluno_encontrado[1]
                        nova_matricula = nova_matricula if nova_matricula else aluno_encontrado[2]
                        codigo_curso = codigo_curso if codigo_curso else aluno_encontrado[4]

                        if nome and not isinstance(nome, str):
                            print(f'\n--------------')
                            print(f'Nome inválido.')
                            print(f'--------------')
                            pausar_execucao()
                            return
                        
                        if isinstance(data_nascimento, datetime.date):
                            data_nascimento = data_nascimento
                        else:    
                            try:
                                datetime.datetime.strptime(data_nascimento, '%Y-%m-%d')
                            except ValueError:
                                print(f'\n------------------------------------------------------') 
                                print(f'Data de nascimento inválida. Use o formato YYYY-MM-DD.')
                                print(f'------------------------------------------------------') 
                                pausar_execucao()
                                return
                            
                        if nova_matricula and (not nova_matricula.isdigit() or len(nova_matricula) != 11):
                            print(f'\n----------------------------------------------------')   
                            print(f'Matricula inválida. Deve conter 11 dígitos numéricos')
                            print(f'----------------------------------------------------') 
                            pausar_execucao()
                            return   
                        
                        if codigo_curso and not isinstance(codigo_curso, str):
                            print(f'\n-------------------------') 
                            print(f'Código do curso inválido.')
                            print(f'-------------------------') 
                            pausar_execucao()
                            return 
                        
                        id_curso_fk = self.curso.buscar_id_curso_por_codigo(codigo=codigo_curso)
                        if id_curso_fk is not None and isinstance(id_curso_fk, tuple):
                            id_curso_fk = id_curso_fk[0]

                        if id_curso_fk is None:
                            print(f'\n---------------------')
                            print(f'Curso não encontrado.')
                            print(f'---------------------')
                            pausar_execucao()
                            return
                        
                        
                        if nova_matricula != aluno_encontrado[2]:
                            aluno_com_matricula = self.aluno.buscar_aluno_por_matricula(matricula=nova_matricula)
                            if aluno_com_matricula:
                                print(f'\n-----------------------------------------------') 
                                print(f'Número de matrícula (CPF) já consta no sistema!')
                                print(f'-----------------------------------------------') 
                                pausar_execucao()
                                return

                        
                        self.aluno.atualizar_aluno(novo_nome=nome, nova_data_nascimento=data_nascimento, nova_matricula=nova_matricula, novo_id_curso_fk=id_curso_fk,matricula=aluno_encontrado[2])
                        print(f'\n-------------------------------')
                        print(f'Aluno atualizado com sucesso!')
                        print(f'-------------------------------')
                        pausar_execucao() 
                    except ValueError:   
                        print(f'\n-----------------------------------------') 
                        print(f'Oops! Um erro ocorreu. Tente novamente...')   
                        print(f'-----------------------------------------') 
                        pausar_execucao()        
                else: 
                    print(f'\n---------------')
                    print(f'Opção Inválida!')
                    print(f'---------------')
                    pausar_execucao()
            except ValueError:   
                print(f'\n-----------------------------------------') 
                print(f'Oops! Um erro ocorreu. Tente novamente...')   
                print(f'-----------------------------------------') 
                pausar_execucao() 
        else:
            print(f'\n-----------------------')
            print(f'Nenhum aluno encontrado')
            print(f'-----------------------')
            pausar_execucao()  
            return None


    def deletar_aluno(self):                  
        limpar_terminal()
        print('\n----------------- EXCLUIR ALUNO -----------------\n')

        aluno_encontrado = self.view_aluno()

        if aluno_encontrado is not None:

            print('\nDeseja excluir aluno?')
            print('[1] Sim')
            print('[0] Não')

            try:
                continuar = int(input('OPÇÃO: '))

                if continuar == 0:
                    True
                elif continuar == 1:
                    matricula = aluno_encontrado[2]
                    self.aluno.deletar_aluno(matricula=matricula)
                    print(f'\n---------------------------')
                    print(f'Aluno excluído com sucesso!')
                    print(f'---------------------------')
                else: 
                    print(f'\n---------------')
                    print(f'Opção Inválida!')
                    print(f'---------------')
                    pausar_execucao()    
            except ValueError:   
                print(f'\n-----------------------------------------') 
                print(f'Oops! Um erro ocorreu. Tente novamente...')   
                print(f'-----------------------------------------') 
                pausar_execucao()     
        else:
            print(f'\n-----------------------')
            print(f'Nenhum aluno encontrado')
            print(f'-----------------------')
            pausar_execucao()  
            return None



