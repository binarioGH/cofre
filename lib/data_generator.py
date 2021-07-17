#-*-coding: utf-8-*-
from random import randint, choice
from codecs import open as copen


class DataGenerator:
	def __init__(self, files={}):
		'''
		Create a container of different dictionaries to generate pseudonames, passwords, and more.
		'''
		self.file_packages = {}
		
		#Load all categories.
		for category in files:

			content = load_file(files[category])

			#If there was no problem while opening the file, save it.
			if content: 
				self.file_packages[category] = content	
				



	def load_file(self, file_path):
		'''
		Attempt to load a dictionary file. 
		Returns a list with all the content or False if the file wasn't opened.
		'''
		try:
			with copen(file_path, "r", encoding='utf-8') as f:
				return f.read().split("\n")


		except:
			return False


	def generate_random_password(self, combination_elements, length):
		'''
		Generate a random password based on a string and a length.
		'''
		new_password = ""

		for i in range(0, length + 1):
			new_password += choice(combination_elements)


		return new_password 