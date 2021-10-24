#-*-coding: utf-8-*-

from lib.cryptography import *



c = CipherHandler()


text = input("Text: ")

key1 = "This is the first key"

encrypted = c.encrypt(text, key1)

decrypted = c.decrypt(encrypted, key1)
print(text)
print(decrypted)

print(text == decrypted)



#If you put 13 As in a row, the 13th will be a % sign...
#This will be good for debugging later...