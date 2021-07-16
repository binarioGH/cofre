#-*-coding: utf-8-*-

from os.path import isfile, isdir
from codecs import open as copen


class Storage:
	def __init__(self, filename="information.json"):

		#self.file will be empty if it is not loaded correctly, else it will have the name of the databasefile
		self.file = ""
		self.data = {}
		
		if isfile(filename):
			self.load_file (filename)

		else:
			self.create_database(filename)
			self.load_file(filename)


	def load_file(self, filename):
		try:
			with copen(filename, 'r', encoding='utf-8') as f:
				content = loads(f.read())

		except:
			self.file = ""
			self.data = {}

		else:
			self.file = filename
			self.data = content 


	def create_database(self, filename):
		content = {}

		with copen(filename, "w", encoding='utf-8') as f:
			f.write(dumps(content))



		'''
		Structure:

		{
			"site name": {
					"logo": "url of site's logo",

					"accounts": [
						{
							"username" : "username",
							"password" : "encrypted password",
						},
						{
							...
						}
					]
				}

			}
		}
		'''

