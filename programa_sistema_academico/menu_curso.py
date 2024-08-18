from curso import Curso
from aluno import Aluno
from utils import limpar_terminal, pausar_execucao

class MenuCurso:
    def __init__(self):
        self.curso = Aluno()
        self.curso = Curso()

    def exibir_menu(self):
        while True:
            limpar_terminal()
            print('\n########## MENU CURSO ##########\n')
            print('[1] Adicionar Curso')
            print('[2] Listar Cursos')
            print('[3] Buscar Curso por código')
            print('[4] Atualizar Curso')
            print('[5] Deletar Curso')
            print('[6] Voltar')
            print('\n################################')

            try:
                opccao = int(input('OPÇÃO: '))

                if opccao == 1:
                    self.adicionar_curso()
                elif opccao == 2:
                    self.listar_cursos()
                elif opccao == 3:
                    self.buscar_curso()
                elif opccao == 4:
                    self.atualizar_curso()
                elif opccao == 5:  
                    self.deletar_curso()
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

    def adicionar_curso(self):
        limpar_terminal()
        print('\n----------------- CADASTRO DE CURSO -----------------\n')
        try:
            codigo = input('Código: ').strip().lower()
            nome = input('Nome: ').strip().lower()
            carga_horaria = float(input('Carga Horária): ')).strip()
            
            
            # validação de código do curso
            if not codigo or not codigo.isdigit():
                print(f'\n-------------------------') 
                print(f'Código do curso inválido.')
                print(f'-------------------------') 
                pausar_execucao()
                return  

            #validação de nome
            if not nome or not isinstance(nome, str):
                print(f'\n--------------')
                print(f'Nome inválido.')
                print(f'--------------')
                pausar_execucao()
                return

            # validação de código de curso
            if not carga_horaria or not isinstance(carga_horaria, (float, int)):
                print(f'\n-------------------------') 
                print(f'Código do curso inválido.')
                print(f'-------------------------') 
                pausar_execucao()
                return
            
            # verifica se já existe cadastro no sistema com a mesma codigo
            curso = Curso(codigo=codigo)

            if curso.buscar_curso():
                print(f'\n-----------------------------------------------')  
                print(f'Número de código de curso já consta no sistema!')
                print(f'-----------------------------------------------') 
                pausar_execucao()
                return
            else:
                curso = Curso(codigo=codigo, nome=nome, carga_horaria=carga_horaria)
                curso.adicionar_curso()
                print(f'\n-----------------------------') 
                print(f'Curso cadastrado com sucesso!')
                print(f'-----------------------------') 
                pausar_execucao()
                return curso
        except ValueError:   
            print(f'\n-----------------------------------------') 
            print(f'Oops! Um erro ocorreu. Tente novamente...')   
            print(f'-----------------------------------------') 
            pausar_execucao()


    def listar_cursos(self):
        limpar_terminal()

        largura_total = 120
        largura_codigo = 20
        largura_nome = 60
        largura_carga_horaria = 20

        cursos = Curso.listar_cursos()
        if cursos is not None:
            print(f'\nRESULTADO:')
            print('-'*largura_total)
            print(f'{"CÓD CURSO":<{largura_codigo}} | {"NOME":<{largura_nome}} | {"CH":<{largura_carga_horaria}}')
            print('-'*largura_total)

            for curso in cursos:
                codigo = curso[0]
                nome = curso[1]
                carga_horaria = f'{curso[2]:.1f}'
                
                print(f'{codigo:<{largura_codigo}} | {nome:<{largura_nome}} | {carga_horaria:<{largura_carga_horaria}}')
                print('-'*largura_total)
                pausar_execucao()
            return cursos
        else:
            print(f'\n-----------------------')  
            print(f'Nenhum curso encontrado')
            print(f'-----------------------')  
            pausar_execucao() 
            return None 

    def view_curso(self):
        largura_total = 120
        largura_codigo = 20
        largura_nome = 60
        largura_carga_horaria = 20
        

        codigo = input('Informe o código do curso: ').strip().lower()

        localizar_curso = Curso(codigo=codigo)
        curso = localizar_curso.buscar_curso()
        if curso is not None:
            print(f'\nRESULTADO:')
            print('-'*largura_total)
            print(f'{"CÓD CURSO":<{largura_codigo}} | {"NOME":<{largura_nome}} | {"CH":<{largura_carga_horaria}}')
            print('-'*largura_total)

            codigo = curso[0]
            nome = curso[1]
            carga_horaria = f'{curso[2]:.1f}'
                
            print(f'{codigo:<{largura_codigo}} | {nome:<{largura_nome}} | {carga_horaria:<{largura_carga_horaria}}')
            print('-'*largura_total)
            return curso
        else:
            return None    
        
    def view_alunos(self, codigo):
        largura_total = 140
        largura_nome = 60
        largura_DN = 20
        largura_matricula = 20
        largura_data_matricula = 20

        curso = Curso(codigo=codigo)
        lista_alunos = curso.buscar_alunos_por_curso()
        if lista_alunos is not None:
            print(f'\nAlunos Matriculados:')
            print('-'*largura_total)
            print(f'{"NOME":<{largura_nome}} | {"DATA NASC":<{largura_DN}} | {"MATRÍCULA(CPF)":<{largura_matricula}} | {"DATA MATRÍCULA":<{largura_data_matricula}}')
            print('-'*largura_total)

            for aluno in lista_alunos:
                nome = aluno[0]
                dataNasc = aluno[1].strftime('%d/%m/%Y')
                matricula = f'{aluno[2][:3]}.{aluno[2][3:6]}.{aluno[2][6:9]}-{aluno[2][9:]}'
                dataMatricula = aluno[3].strftime('%d/%m/%Y')

                print(f'{nome:<{largura_nome}} | {dataNasc:<{largura_DN}} | {matricula:<{largura_matricula}} | {dataMatricula:<{largura_data_matricula}}')
                print('-'*largura_total)
                pausar_execucao()
            return lista_alunos
        else:
            print(f'\n-----------------------')  
            print(f'Nenhum aluno encontrado')
            print(f'-----------------------')  
            pausar_execucao() 
            return None 
           

    def buscar_curso(self):
        limpar_terminal()
        print('\n----------------- LOCALIZAR CURSO -----------------\n')
        
        localizar_curso = self.view_curso()

        if localizar_curso is not None:
            print(f'')
            codigo = localizar_curso[0]
            self.view_alunos(codigo=codigo)
            pausar_execucao()
            return localizar_curso
        else:
            print(f'\n-----------------------')
            print(f'Nenhum curso encontrado')
            print(f'-----------------------')
            pausar_execucao()  
            return None

    def atualizar_curso(self):
        limpar_terminal()
        print('\n----------------- ATUALIZAR CURSO -----------------\n')

        curso_encontrado = self.view_curso()

        if curso_encontrado is not None:

            print('\nDeseja atualizar curso?')
            print('[1] Sim')
            print('[0] Não')
            try:
                continuar = int(input('OPÇÃO: '))

                if continuar == 0:
                    True
                elif continuar == 1:
                    limpar_terminal()
                    print('\n------------------------ ATUALIZAR CURSO ------------------------\n')
                    try:
                        codigo = input('Código (ou clique ENTER para não alterar): ').strip().lower()
                        nome = input('Nome (ou clique ENTER para não alterar): ').strip().lower()
                        carga_horaria = float(input('Carga Horária (ou clique ENTER para não alterar): ')).strip().lower()
                        

                        codigo = codigo if codigo else curso_encontrado[0]
                        nome = nome if nome else curso_encontrado[1]
                        carga_horaria = carga_horaria if carga_horaria else curso_encontrado[2]


                        if codigo and not codigo.isdigit():
                            print(f'\n-------------------------') 
                            print(f'Código do curso inválido.')
                            print(f'-------------------------') 
                            pausar_execucao()
                            return  
                        
                        if nome and not isinstance(nome, str):
                            print(f'\n--------------')
                            print(f'Nome inválido.')
                            print(f'--------------')
                            pausar_execucao()
                            return
                        
                        if carga_horaria and not isinstance(carga_horaria, (float, int)):
                            print(f'\n-------------------------') 
                            print(f'Código do curso inválido.')
                            print(f'-------------------------') 
                            pausar_execucao()
                            return 
                        
                        curso = Curso(codigo=codigo)
                        localizar_curso = curso.buscar_curso()
                        if localizar_curso and curso_encontrado[0] != codigo:
                            print(f'\n-----------------------------------------------')  
                            print(f'Número de código de curso já consta no sistema!')
                            print(f'-----------------------------------------------') 
                            pausar_execucao()
                            return

                        curso = Curso(codigo=codigo, nome=nome, carga_horaria=carga_horaria)
                        curso.atualizar_curso()
                        print(f'\n-----------------------------')
                        print(f'Curso atualizado com sucesso!')
                        print(f'-----------------------------')
                        return curso
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
            print(f'Nenhum curso encontrado')
            print(f'-----------------------')
            pausar_execucao()  
            return None


    def deletar_curso(self):                  
        limpar_terminal()
        print('\n----------------- EXCLUIR CURSO -----------------\n')

        curso_encontrado = self.view_curso()

        if curso_encontrado is not None:

            print('\nDeseja excluir curso?')
            print('[1] Sim')
            print('[0] Não')

            try:
                continuar = int(input('OPÇÃO: '))

                if continuar == 0:
                    True
                elif continuar == 1:
                    codigo = curso_encontrado[0]
                    curso = Curso(codigo=codigo)
                    curso.deletar_curso()
                    print(f'\n---------------------------')
                    print(f'curso excluído com sucesso!')
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
            print(f'Nenhum curso encontrado')
            print(f'-----------------------')
            pausar_execucao()  
            return None


