import unittest

from logica import sessao

class TestSessao(unittest.TestCase):

    def setUp(self):
        sessao.remover_todas_sessoes()

    def test_sem_sessao(self):
        sessoes = sessao.listar_sessoes()
        self.assertEqual(0,len(sessoes))

    def test_adicionar_uma_sessao(self):
        sessao.adicionar_sessao(2,"Guardiões da Galáxia",10)

        sessoes=sessao.listar_sessoes()
        self.assertEqual(1,len(sessoes))

        s= sessoes[0]

        self.assertEqual(2,s[0])
        self.assertEqual("Guardiões da Galáxia",s[1])
        self.assertEqual(10,s[2])

    def test_adicionar_duas_sessoes(self):
        sessao.adicionar_sessao(2,"Guardiões da Galáxia",10)
        sessao.adicionar_sessao(5,"Star Wars",20)

        sessoes = sessao.listar_sessoes()
        self.assertEqual(2,len(sessoes))

    def test_buscar_sessao(self):

        sessao.adicionar_sessao(2,"Guardiões da Galáxia",10)
        sessao.adicionar_sessao(5,"Star Wars",20)

        s = sessao.buscar_sessao(2)
        self.assertEqual(2,s[0])
        self.assertEqual("Guardiões da Galáxia",s[1])
        self.assertEqual(10,s[2])

    def test_remover_sessao(self):
        sessao.adicionar_sessao(2,"Guardiões da Galáxia",10)
        sessao.adicionar_sessao(5,"Star Wars",20)

        sessao.remover_sessao(2)

        s = sessao.buscar_sessao(2)
        self.assertIsNone(s)

    def test_remover_todas_sessoes(self):
        sessao.adicionar_sessao(2,"Guardiões da Galáxia",10)
        sessao.adicionar_sessao(5,"Star Wars",20)

        sessao.remover_todas_sessoes()

        s = sessao.listar_sessoes()
        self.assertEqual([],s)

    def test_iniciar_sessoes(self):
        sessao.iniciar_sessoes()
        sessoes = sessao.listar_sessoes()
        self.assertEqual(2,len(sessoes))

if __name__ == '__main__':
    unittest.main(exit=False)
        

                   

                         
                                        
                   

                                      
                         
