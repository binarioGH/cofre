#-*-coding: utf-8-*-
import eel
from json import loads, dump
from json.decoder import JSONDecodeError
from lib.data_management import *
from lib.data_generator import *
from lib.cryptography import *
from codecs import open as copen
from random import randint
import pyperclip

TOOLS = {
	"DATAGEN": DataGenerator(),
	"STORAGE": Storage('cli_info.json'),
	"CRYPTO": CipherHandler()
}


@eel.expose
def create_backup():
	if not 'backup' in TOOLS['STORAGE'].data:
		TOOLS['STORAGE'].data['backup'] = {}

	TOOLS['STORAGE'].data['backup'].update(TOOLS['STORAGE'].data['sites'])
	del TOOLS['STORAGE'].data['sites']
	TOOLS['STORAGE'].data['sites'] = {}
	TOOLS['STORAGE'].save_data()

@eel.expose
def is_checksum_empty():
	if len(TOOLS['STORAGE'].data['checksum']) != 128:
		return False

	return True





@eel.expose
def change_master_password(last_password, new_password):
	if not is_checksum_empty():
		TOOLS['STORAGE'].set_checksum(new_password, TOOLS['CRYPTO'])
		return 0

	elif check_password(last_password):
		TOOLS['STORAGE'].set_checksum(new_password, TOOLS['CRYPTO'])
		for site in TOOLS['STORAGE'].data['sites']:
			for account in   TOOLS['STORAGE'].data['sites'][site]['accounts']:
				current_password = TOOLS['STORAGE'].data['sites'][site]['accounts'][account]

				unencrypted_password = decrypt(last_password, current_password)

				encrypted_new_password = encrypt(last_password, unencrypted_password)

				TOOLS['STORAGE'].data['sites'][site]['accounts'][account] = encrypted_new_password

		TOOLS['STORAGE'].save_data()
		return 0

	elif last_password == new_password:
		return -1

	return -2

@eel.expose
def new_password():
	combination = TOOLS['CRYPTO'].abc
	random_length = randint(12, 20) 
	return TOOLS['DATAGEN'].generate_random_password(combination, random_length)


@eel.expose
def add_new_account(site, account, password):
	TOOLS['STORAGE'].save_new_user(site, account, password)






@eel.expose
def notify(message):
	#TODO: Toast notification.
	print(message)
	

@eel.expose
def encrypt(key, password):
	result = TOOLS['CRYPTO'].encrypt(password, key)
	return result

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