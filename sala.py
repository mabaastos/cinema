
salas =[]

def adicionar_sala(numero,sessao,condicao):

    sala = [numero,sessao,condicao]
    salas.append(salas)

def listar_salas():
     return salas

def remover_sala(numero):
    for s in salas:
        if s[0] == numero:
            salas.remove(s)
            return True
        return None
    
def buscar_sala (numero):
    for s in salas:
        if s[0] == numero:
            return s
        return None
def remover_todas_salas():
    global salas
    salas = []
    
    

def iniciar_salas ():
    adicionar_sala(4,10,"Sim")
    adicionar_sala(3,12,"não")
    
    
