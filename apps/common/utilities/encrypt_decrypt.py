from Crypto.Cipher import XOR
import base64
from settings import SECRET_KEY


def encrypt(plaintext, key=SECRET_KEY):
  cipher = XOR.new(key)
  return base64.b64encode(cipher.encrypt(plaintext))

def decrypt(ciphertext, key=SECRET_KEY):
  cipher = XOR.new(key)
  return cipher.decrypt(base64.b64decode(ciphertext))
