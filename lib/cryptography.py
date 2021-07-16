#-*-coding: utf-8-*-



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
		pass


	def decrypt(self, text, key):
		pass



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

				if mode == "e":
					pass

				elif mode == "d":
					pass

			#I dont know if the key index should be += 1 when the current_index == -1...
			#Must ask in cryptography forums later.
			key_index += 1

		return translated_word
