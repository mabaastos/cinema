import unittest

from logica import filme

class TestFilme(unittest.TestCase):
    
     def setUp(self):
         filme.remover_todos_filmes()

     def test_sem_filmes(self):
         filmes = filme.listar_filmes()
         self.assertEqual(0,len(filmes))

    def test_adicionar_um_filme(self):
        filme.adicionar_filme("Star wars",12,150,"ação")

        filmes= filme.listar_filmes()
        self.assertEqual(1,len(filmes))

        f = filmes[0]

        self.assertEqual("Star wars",m[0])
        self.assertEqual(12,m[1])
        self.assertEqual(150,m[2])
        self.assertEqual("ação",m[3])

    def test_adicionar_dois_filmes (self):
        filme.adicionar_filme("Star wars",12,150,"ação")
        filme.adicionar_filme("Titanic",10,160,"drama")

        filmes = filme.listar_filmes()
        self.assertEqual(2,len(filmes))

    def test_buscar_filme(self):
        filme.adicionar_filme("Star wars",12,150,"ação")
        filme.adicionar_filme("Titanic",10,160,"drama")

        f = filme.buscar_filme("Star wars")
        self.assertEqual("Star wars",m[0])
        self.assertEqual(12,m[1])
        
     def test_remover_filme(self):
        filme.adicionar_filme("Star wars",12,150,"ação")
        filme.adicionar_filme("Titanic",10,160,"drama")

        filme.remover_filme("Star wars")

        f =filme.buscar_filme("Star wars")
        self.assertIsNone(f)

    def test_remover_todos_filmes(self):
        filme.adicionar_filme("Star wars",12,150,"ação")
        filme.adicionar_filme("Titanic",10,160,"drama")

        filme.remover_todos_filmes()

        f=filme.listar_filmes()
        self.assertEqual([],f)
        
    def test_iniciar_medicos(self):
        filme.iniiciar_filmes()
        filmes = filme.listar_filmes()
        self.assertEqual(2,len(filmes))

if __name__=='__main___':
    unittest.main(exit=False)
    
        
    
        
