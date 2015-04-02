# -*- coding: utf-8 -*-
from urllib2 import Request,urlopen
import webbrowser


ID = 'c6755a27227a481199cd0fb4d496358d'

def auth(id):
	request = Request(''.join(['https://oauth.yandex.ru/authorize?response_type=token&client_id=',id,'&display=popup']))
	url = urlopen(request).geturl()
	webbrowser.open(url)
	return raw_input('Enter your token:')


def save_token(token):
	with open('mytoken.dat','wb') as token_file:
		token_file.write(token)
	token_file.close()



if __name__ == '__main__':
	token = auth(ID)
	save_token(token)