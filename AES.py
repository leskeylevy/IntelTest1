"AES. The Advanced Encryption Standard (AES) is the trusted standard algorithm used by the United States government, as well as other organizations. Although extremely efficient in the 128-bit form, AES also uses 192- and 256-bit keys for very demanding encryption purposes. AES is widely considered invulnerable to all attacks except for brute force. Regardless, many internet security experts believe AES will eventually be regarded as the go-to standard for encrypting data in the private sector."

import sys
import base64
from Crypto.Cipher import AES


class AESCipher(object):
    def __init__(self, key):
        self.bs = 16
        self.cipher = AES.new(key, AES.MODE_ECB)

    def encrypt(self, raw):
        raw = self._pad(raw)
        encrypted = self.cipher.encrypt(raw)
        encoded = base64.b64encode(encrypted)
        return str(encoded, 'utf-8')

    def decrypt(self, raw):
        decoded = base64.b64decode(raw)
        decrypted = self.cipher.decrypt(decoded)
        return str(self._unpad(decrypted), 'utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    def _unpad(self, s):
        return s[:-ord(s[len(s)-1:])]


if __name__ == '__main__':
    key = '`?.F(fHbN6XK|j!t'
    cipher = AESCipher(key)

    plaintext = '542#1504891440039'
    encrypted = cipher.encrypt(plaintext)
    print('Encrypted: %s' % encrypted)
    ciphertext = '5bgJqIqFuT8ACuvT1dz2Bj5kx9ZAIkODHWRzuLlfYV0='
    assert encrypted == ciphertext

    decrypted = cipher.decrypt(encrypted)
    print('Decrypted: %s' % decrypted)
    assert decrypted == plaintext