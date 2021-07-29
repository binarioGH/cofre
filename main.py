#-*-coding: utf-8-*-
import eel
from json import loads, dump
from json.decoder import JSONDecodeError
from lib.data_management import *
from lib.data_generator import *
from lib.cryptography import *
from codecs import open as copen


TOOLS = {
	"DATAGEN": DataGenerator(),
	"STORAGE": Storage('cli_info.json'),
	"CRYPTO": CipherHandler()
}

	

@eel.expose
def get_accounts():
	accounts = []

	for site in TOOLS['STORAGE'].data['sites']:
		for account in TOOLS['STORAGE'].data['sites'][site]['accounts']:
			accounts.append({
				"site": site,
				"user": account,
				"hashed_password": TOOLS['STORAGE'].data['sites'][site]['accounts'][account]
				})

	return accounts


def on_close(page, sockets):
	print(page, 'closed')
	print('Still have sockets open to', sockets)

def main():
	web_options = {
		"mode": "chrome-app",
		"host": "localhost",
		"port": 8000
	}
	eel.init("GUI")

	eel.start("index.html",  size=(1216, 739), callback=on_close)
	#storage = Storage()


if __name__ == '__main__':
	main()