from logica import sessao

def imprimir_sessoes(sessao):
    print("Sala:",sessao[0])
    print("Filme:",sessao[1])
    print("Codigo da sessão:",sessao[2])
    print()
    
def menu_adicionar():
    print("\n Adicionar sessão \n")
    sala = int(input("Número da sala:"))
    filme = str(input("Filme:"))
    codigo = int(input("Codigo da sessão:"))

def menu_listar():
    print("\n Listar sessões \n")
    sessoes = sessao.listar_sessoes()
    for s in sessoes:
        imprimir_sessoes(sessao)

def menu_buscar():
    print("\n Buscar sessão \n")
    codigo = int(input("Insira o código da sessão:"))
    s = sessao.buscar_sessao(codigo)
    if s == None:
        print("Sessão não encontrada.")
    else:
        imprimir_sessoes(s)
        
def menu_remover():
    print("\n Remover sala \n ")
    codigo = int(input("Insira o código da sessão:"))
    s = sessao.remover_sessao(codigo)
    if s == False :
        print("Sessão não encontrada.")
    else:
        print("Sessão removida.")
        
def mostrar_menu():
    run_sessao = True
    menu = ("\n----------------\n"+
             "(1) Adicionar sessão \n" +
             "(2) Listar sessão \n" +
             "(3) Buscar sessão \n" +
             "(4) Remover sessão \n" +
             "(0) Voltar\n"+
            "----------------")
    while run_sessao :
        print(menu)
        x = int(input("Digite a operação que deseja realizar:"))

        if x == 1:
            menu_adicionar()
        elif x == 2:
            menu_listar()
        elif x == 3 :
            menu_buscar()
        elif x == 4 :
            menu_remover()
        elif x == 0:
            run_sala = False 

    
    
    
                     
