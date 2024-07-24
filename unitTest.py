# test_vigenere_decrypt.py

import unittest
from VigenereCipherDecoder import vigenere_decrypt

class TestVigenereDecrypt(unittest.TestCase):
    def test_simple_case(self):
        self.assertEqual(vigenere_decrypt('RIJVS', 'KEY'), 'HELLO')
    
    def test_with_spaces(self):
        self.assertEqual(vigenere_decrypt('RIJ VS', 'KEY'), 'HEL LO')
    
    def test_long_key(self):
        self.assertEqual(vigenere_decrypt('RIJVS', 'VERYLONGKEY'), 'HELLO')

if __name__ == '__main__':
    unittest.main()
