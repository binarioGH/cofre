#-*-coding: utf-8-*-
import eel
from json import loads, dump
from lib.data_management import *


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