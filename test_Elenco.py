import unittest
import Elenco

class Testelenco(unittest.TestCase):

    def setUp(self):
        Elenco.remover_todos_elencos()

    def test_sem_elencos(self):
        elencos = Elenco.listar_elenco()
        self.assertEqual(0, len(elencos))

        
if __name__ == '__main__':
    unittest.main(exit=False)
