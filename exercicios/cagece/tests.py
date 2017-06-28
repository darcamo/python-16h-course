import unittest
from funcoes import *


# Asserts mais úteis para os unittests:
# - assertEqual
# - assertAlmostEqual
# - assertTrue
# - assertFalse
# - fail


class ExercicioCageceTestCase(unittest.TestCase):
    def test_dobra(self):
        self.assertEqual(dobra(2), 4)
        self.assertEqual(dobra(-16), -32)
        self.assertAlmostEqual(dobra(5.7), 11.4)
        self.assertAlmostEqual(dobra(1/3), 2/3)

    def test_calc_faixas_consumo(self):
        # A lista retornada pela função calc_faixas_consumo sempre deve ter 5
        # elementos independentemente do valor do consumoxs
        self.assertEqual(len(calc_faixas_consumo(17)), 5)
        self.assertEqual(len(calc_faixas_consumo(3)), 5)
        self.assertEqual(len(calc_faixas_consumo(10)), 5)

        # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        # xxxxxxxxxx Continuar os testes xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

        # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


    def test_calc_custo_agua(self):
        pass


    def test_calc_custo_esgoto(self):
        pass


# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
if __name__ == '__main__':
    unittest.main()
