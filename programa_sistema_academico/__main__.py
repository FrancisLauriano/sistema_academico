from menu_aluno import MenuAluno
from menu_curso import MenuCurso
from time import sleep
from utils import limpar_terminal, pausar_execucao

class MenuPrincipal:
    def __init__(self):
        self.menu_aluno = MenuAluno()
        self.menu_curso = MenuCurso()


    def exibir_menu(self):
        while True:
            limpar_terminal()
            print(f'\n#################### MENU PRINCIPAL ####################\n')
            print(f'[1] Gerenciar Alunos')
            print(f'[2] Gerenciar Cursos')
            print(f'[0] Sair')
            print(f'\n########################################################')

            try:
                opcao = int(input('OPÇÃO: '))
                limpar_terminal()

                if opcao == 1:
                    self.menu_aluno.exibir_menu()
                elif opcao == 2:
                    self.menu_curso.exibir_menu() 
                elif opcao == 0:
                    limpar_terminal()
                    print(f'Encerrando o sistema...')
                    print(f'|'*5)
                    sleep(0.1)
                    print(f'|'*4)
                    sleep(0.1)
                    print(f'|'*3)
                    sleep(0.1)
                    print(f'|'*2)
                    sleep(0.1)
                    print(f'|'*1)
                    sleep(0.1)
                    print(f'FINALIZADO')
                    break    
                else:
                    print('\n----------------------------------')    
                    print('Opção Inválida. Tente novamente...')
                    print('----------------------------------') 
                    pausar_execucao()            

            except ValueError:
                print(f'\n------------------------------')
                print(f'Oops!  No valid.  Try again...')   
                print(f'------------------------------')  
                pausar_execucao()   

if __name__ == '__main__':
    menu_principal = MenuPrincipal()
    menu_principal.exibir_menu()
