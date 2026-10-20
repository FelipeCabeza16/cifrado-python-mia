import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from cifrado.logica import cifrar, descifrar, validar_numero


class PruebasCifrado(unittest.TestCase):
    def test_caso_123456(self):
        self.assertEqual(cifrar("123456"), "018932")
        self.assertEqual(descifrar("018932"), "123456")

    def test_caso_791658(self):
        self.assertEqual(cifrar("791658"), "834652")
        self.assertEqual(descifrar("834652"), "791658")

    def test_conserva_ceros_a_la_izquierda(self):
        self.assertEqual(descifrar(cifrar("000123")), "000123")

    def test_ida_y_vuelta(self):
        for n in range(0, 1_000_000, 997):
            texto = f"{n:06d}"
            self.assertEqual(descifrar(cifrar(texto)), texto)

    def test_entradas_invalidas(self):
        for malo in ("", "12345", "1234567", "12a456", "12 456", "-12345", "１２３４５６"):
            with self.assertRaises(ValueError):
                validar_numero(malo)


if __name__ == "__main__":
    unittest.main()
