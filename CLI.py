#-*-coding: utf-8-*-
from lib.cryptography import *
from lib.data_management import *
from lib.data_generator import *
from pyperclip import copy
from json import dumps


def CLI(cmd, storage, generator,crypto):
	cmd = cmd.lower()

	if cmd == "adduser":
		site = input("Site name: ")
		user = input("Username: ")
		key = input("Key Phrase: ")
		password_length = int(input("Enter password length: "))
		generated_password = generator.generate_random_password(crypto.abc, password_length)

		encrypted_password = crypto.encrypt(generated_password, key)
		storage.save_new_user( site, user, encrypted_password)
		print('''Site: {}
			User: {}'''.format(site, user))
		q_copy = input("Wanna Copy the password? [y/n]").lower()

		if q_copy == 'y':
			copy(generated_password)
			print("Copied password to the clipboard.")


	elif cmd == "dumps":
		content = dumps(storage.data, indent=4)

		print(content)

	elif cmd == 'password':
		print("Sites: ")
		for site in storage.data['sites']:
			print(site)
		site = input("What site are you looking for?")
		if not site in storage.data['sites']:
			print("Couldn't find that site, check the smelling.")
			return -1

		if not 'accounts' in storage.data['sites'][site]:
			print("This site is empty...")
			return -1

		username = input("What username are you looking for?")
		if username in storage.data['sites'][site]['accounts']:
			key = input("Enter your key phrase: ")
			if crypto.checksum(key, storage.data['checksum']):
				password = crypto.decrypt(storage.data['sites'][site]['accounts'][username], key)
				print("Copying password in your clipboard")
				copy(password)
			else:
				print("Key phrase is incorrect.")

		else:
			print("Couldn't find the username, try again.")
			return -1




def main():
	storage = Storage("cli_info.json")
	crypto = CipherHandler()
	generator = DataGenerator()
	storage.set_checksum(
		input("Set the key phrase: "),
		crypto
	)
	
	cmd = ""

	while cmd != "exit":
		cmd = input(">>>")
		CLI(cmd, storage, generator,crypto)


if __name__ == '__main__':
	main()