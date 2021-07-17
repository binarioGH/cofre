#-*-coding: utf-8-*-

from os.path import isfile, isdir
from codecs import open as copen
from json import dumps, loads


class Storage:
	def __init__(self, filename="information.json"):

		#self.file will be empty if it is not loaded correctly, else it will have the name of the databasefile
		self.file = ""
		self.data = {}
		
		if isfile(filename):
			self.load_file(filename)

		else:
			self.create_database(filename)


	def load_file(self, filename):
		try:
			with copen(filename, 'r', encoding='utf-8') as f:
				content = loads(f.read())

		except Exception as e:
			print(e)
			print("Couldn't load the file.")
			self.file = ""
			self.data = {}

		else:
			self.file = filename
			self.data = content 


	def save_new_user(self, site, user, password):
		'''
		Save data to the database.
		'''

		if site in self.data['sites']:
			self.data['sites'][site]['accounts'][user] = password

		else:
			self.data['sites'][site] = {
				"accounts": {
					user: password
				}
			}

		self.save_data()

	def set_checksum(self, key_phrase, crypto):
		self.data['checksum'] = crypto.return_hashed_string(key_phrase)
	


	def create_database(self, filename):
		content = {
			'sites': {},
			'checksum' : ""
		}

		self.data = content
		self.file = filename
		self.save_data()



		'''
		Structure:

		{
			"sites": {
				"site name": {

						"accounts": 
							{
								"username" : "password"
							},
						
					}
				}
			},
			"checksum" : "SHA512 hash"
		}
		'''

	def save_data(self):
		'''
		Store data in file.
		'''
		try:
			with copen(self.file, "w", encoding='utf-8') as f:
				dump_data = dumps(self.data, indent=4)
				print(dump_data)
				f.write(dump_data)

		except Exception as e:
			print(e)
			self.file = ""