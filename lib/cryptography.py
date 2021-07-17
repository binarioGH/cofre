#-*-coding: utf-8-*-
from hashlib import sha512


class CipherHandler:
	def __init__(self):

		'''
		I will work to get all utf-8 characters in an optimal way.
		'''


		#Add letters to the alphabet
		self.abc = "abcdefghijklmnopqrstuvwxyz"
		self.abc += self.abc.upper()

		#Add special characters
		self.abc += "1234567890+-*/!@#$%^&*()=~"



	def encrypt(self, text, key):
		return self.translate(text, key, "e")


	def decrypt(self, text, key):
		return self.translate(text, key, "d")



	def translate(self, text, key, mode):
		'''
		Encrypt or decrypt text with vigenere cipher.

		mode:
		  'e' -> encryption
		  'd' -> decryption
		'''

		#Store the encrypted or decrypted text.
		translated_word = ""

		#key to iterate trough the key
		key_index = 0

		#Iterate trough the text to encrypt it.
		for character in text:

			#Restart key index
			if key_index == len(key) - 1:
				key_index = 0

			current_index = self.abc.find(character)

			if current_index == -1:
				#I belive this is a bad practice, must investigate.
				translated_word += character

			else:

				# The number that will be added or substracted.
				current_numeric_key = self.abc.find(  key[key_index]  ) + 1


				'''
				In both modes, it is going to be checked if the current index is bigger or lower than it is
				supposed to be, and if it is, it will be moduled by the lenght of the alphabet.
				'''

				if mode == "e":
					current_index -= current_numeric_key
					
					if current_index <= -len(self.abc):
						current_index %= -len(self.abc)


				elif mode == "d":
					current_index += current_numeric_key

					if current_index >= len(self.abc):
						current_index %= len(self.abc)

				translated_word += self.abc[current_index]




			#I dont know if the key index should be += 1 when the current_index == -1...
			#Must ask in cryptography forums later.
			key_index += 1

		return translated_word

	def checksum(self, password, old_hash):
		new_hashed_password = sha512(password.encode()).hexdigest()

		if new_hashed_password == old_hash:
			return True

		return False


	def return_hashed_string(self, text):
		hashed = sha512(text.encode()).hexdigest()
		return hashed