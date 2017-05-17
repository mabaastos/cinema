filmes =[]

def adicionar_filme(nome,classi,duracao,genero):
    filme=[nome,classi,duracao,genero]
    filmes.append(filmes)
    
def listar_filmes():
    return filmes

def remover_filme(nome):
    for f in filmes:
        if f[0] == nome:
            filmes.remove(f)
            return True
        return None
    
def buscar_filme(nome):
    for f in filmes:
        if f[0] == nome:
            return f
        return None
def remover_todos_filmes():
    global filmes
    filmes = []
    
def iniciar_filmes():
    adicionar_filme("Star wars",12,150,"ação")
    adicionar_filme("Titanic",10,160,"drama")
