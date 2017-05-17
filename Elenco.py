elencos=[]

import Ator
import Filme


def adicionar_ator(cod_elenco,cod_ator,cod_filme,tipo):
    elenco=[cod_elenco,cod_ator,cod_filme,tipo]
    elencos.append(elenco)

def consultar_atores_por_filme(cod_elenco):
    pass

def remover_elenco(cod_elenco):
    for e in elencos:
        if (e[0]==cod_elenco):
            elencos.remove(e)
            return True
    return False

def buscar_elenco(cod_elenco):
    for e in elencos:
        if (e[0] == cod_elenco):
            return e
    return None

def listar_elenco():
    return elencos

def buscar_elenco_por_filme(cod_filme):
    for f in filmes:
        if (f[0] == cod_filme):
            return e
    return None

def remover_todos_elencos():
    global elencos
    elencos=[]

def inicar_elencos():
    cadastrar_elenco(111, 555, 888, "terror")
    cadastrar_elenco(145, 453, 789, "suspense")
