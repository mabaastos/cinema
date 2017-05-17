from logica import sala
from gui import menu_salas

from logica import sessao
from gui import menu_sessao

from logica import filme
from gui import menu_filme


def inicializar_dados():
    sala.iniciar_salas()
    sessao.iniciar_sessoes()
    filme.iniciar_filmes()
                           

def mostrar_menu():
    run_menu = True

    inicializar_dados()

    menu =("\n----------------\n"+
             "(1) Menu salas \n" +
             "(2) Menu sessões \n" +
             "(3) Menu filmes \n" +
             "(0) Sair\n"+
            "----------------")
    while (run_menu):
        print(menu)
        x = int (input("Insira a opção desejada:"))

        if x == 1:
            menu_salas.mostrar_menu()
        elif x == 2:
            menu_sessao.mostrar_menu()
        elif x == 3:
            menu_filme.mostrar_menu()
        elif x ==0:
            run_menu=False
        else:
            print("Inválido")
    
