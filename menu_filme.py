from logica import filme

def imprimir_filmes(filmes):
    print("Titulo do filme:",filme[0])
    print("Classificação indicativa:",filme[1])
    print("Duração:",filme[2])
    print("Genero:",filme[3])
    print()
    
def menu_adicionar():
    print("\n Adicionar filme \n")
    nome = str(input("Nome do filme:")).lower()
    classi = int(input("Classificação indicativa:"))
    duracao = int(input("Duração:"))
    genero = str(input("Genero:"))

def menu_listar():
    print("\n Listar filmes \n")
    filmes = filme.listar_filmes()
    for f in filmes:
        imprimir_filmes(filmes)
                  
def menu_buscar():
    print("\n Buscar filme \n")
    nome = str(input("Nome do filme:")).lower()
    f = filme.buscar_filme(nome)
    if f == None :
        print("Filme não encontrado.")
    else:
        imprimir_filmes(f)
                  
def menu_remover():
    print("\n Remover filme \n")
    nome = str(input("Nome do filme:"))
    f = filme.remover_filme(nome)
    if f == False:
        print("Filme não encontrado")
    else:
        print("Filme removido.")
                  
def mostrar_menu ():
    run_filme = True
    menu = ("\n----------------\n"+
             "(1) Adicionar filme \n" +
             "(2) Listar filmes \n" +
             "(3) Buscar filme  \n" +
             "(4) Remover filme \n" +
             "(0) Voltar\n"+
            "----------------")
    while run_filme :
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
            run_filme = False 

                 
            
