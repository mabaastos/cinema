import unittest

from logica import sala

class TestSala(unittest.TestCase):

    def setUp(self):
        sala.remover_todas_salas()

    def test_sem_salas(self):
        
        salas =sala.listar_salas()
        self.assertEqual(0,len(salas))
        
    def test_adicionar_sala(self):
        sala.adicionar_sala(10,2,"sim"):
            
        salas = sala.listar_salas()
        self.assertEqual(1,len(salas))

        s = salas[0]

        self.assertEqual(10,s[0])
        self.assertEqual(2,s[1])
        self.assertEqual("sim",s[2])
        
    def teste_adicionar_duas_salas(self):
        salas.adicionar_sala(10,2,"sim")
        salas.adicionar_sala(15,5,"nao")

        salas = sala.listar_salas()
        self.assertEqual(2,len(salas))

    def test_buscar_sala(self):
        sala.adicionar_sala(10,2,"sim")
        sala.adicionar_sala(15,5,"não")

        s = sala.buscar_sala(15)

        self.assertEqual(15,m[0])
        self.assertEqual(5,m[1])

    def test_remover_sala(self):
        sala.adicionar_sala(10,2,"sim")
        sala.adicionar_sala(15,5,"não")

        sala.remover_sala(15)
        
        s = sala.buscar_sala(15)
        self.assertIsNone(s)
        
    def test_remover_todas_salas(self):
        sala.adicionar_sala(10,2,"sim")
        sala.adicionar_sala(15,5,"não")

        sala.remover_todas_salas()

        s = sala.listar_salas()
        self.assertEqual([],s)

    def test_iniciar_salas(self):
        sala.iniciar_salas()
        salas = sala.listar_salas()
        self.assertEqual(2,len(salas))

if __name__ == '__main__':
    unittest.main(exit=False)

        

        

        
        
        
        
    
