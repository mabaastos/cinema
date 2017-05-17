from logica import sala


def imprimir_salas(sala):
    print ("Número da sala:", sala[0])
    print ("Sessão:",sala[1])
    print ("Condição da sala:",sala [2])
    print ()

def menu_adicionar ():
    print ("\n Adicionar Sala \n ")
    numero = int(input("Número da sala:"))
    sessão = int(input("Sessão:"))
    condicao = str(input ("Sala em manutenção?"))

def menu_listar ():
    print("\n Listar Salas \n")
    salas = sala.listar_salas()
    for s in salas:
        imprimir_salas(s)
        
def menu_buscar():
    print ("\n Buscar Salas \n")
    numero = int (input("Numero da sala:"))
    s = sala.buscar_sala(numero)
    if s == None :
        print("Sala não encontrada.")
    else:
        imprimir_salas(s)

def menu_remover ():
    print ("\n Remover sala \n")
    numero = int(input("Numero da sala:"))
    s = sala.remover_sala(numero)
    if s == False:
        print("Sala não encontrada.")
    else:
        print("Sala removida.")

def mostrar_menu ():
    run_sala = True
    menu = ("\n----------------\n"+
             "(1) Adicionar sala \n" +
             "(2) Listar salas \n" +
             "(3) Buscar sala  \n" +
             "(4) Remover sala \n" +
             "(0) Voltar\n"+
            "----------------")
    while run_sala :
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
