#-*-coding: utf-8-*-
import eel
from json import loads, dump
from json.decoder import JSONDecodeError
from lib.data_management import *
from lib.data_generator import *
from lib.cryptography import *
from codecs import open as copen
import pyperclip

TOOLS = {
	"DATAGEN": DataGenerator(),
	"STORAGE": Storage('cli_info.json'),
	"CRYPTO": CipherHandler()
}



@eel.expose
def notify(message):
	#TODO: Toast notification.
	print(message)
	

@eel.expose()
def decrypt(key, hashed_pass, copy_to_clipboard=True):
	result = TOOLS['CRYPTO'].decrypt(hashed_pass, key)

	if copy_to_clipboard:
		pyperclip.copy(result)

	return result


@eel.expose
def copy(text):
	pyperclip.copy(text)

@eel.expose
def get_accounts():
	'''
	return list of account information, containing site, username and hashed password.
	'''
	accounts = []

	for site in TOOLS['STORAGE'].data['sites']:
		for account in TOOLS['STORAGE'].data['sites'][site]['accounts']:
			accounts.append({
				"site": site,
				"user": account,
				"hashed_password": TOOLS['STORAGE'].data['sites'][site]['accounts'][account]
				})

	return accounts



@eel.expose
def check_password(password):
	return TOOLS['CRYPTO'].checksum(password, TOOLS['STORAGE'].data['checksum'])


def on_close(page, sockets):
	print(page, 'closed')
	print('Still have sockets open to', sockets)

def main():
	eel.init("GUI")
	eel.start("index.html",  size=(1216, 739), callback=on_close)



if __name__ == '__main__':
	main()