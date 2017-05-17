sessoes =[]

def adicionar_sessao(sala,filme,codigo):
    sessao =[sala,filme,codigo]
    sessoes.append(sessoes)
    
def listar_sessoes():
    return sessoes

def remover_sessao(codigo):
    for s in sessoes :
        if s[2] == horario:
            sessoes.remove(s)
            return True
        return None

def buscar_sessao(codigo):
    for s in sessoes:
        if s[2] == codigo:
            return s
        return None
def remover_todas_sessoes():
    global sessoes
    sessoes = []
    
def iniciar_sessoes():
    adicionar_sessao(2,"Guardiões da Galáxia",10)
    adicionar_sessao(5,"Star Wars",20)
                   

