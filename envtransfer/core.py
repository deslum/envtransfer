# -*- coding: utf-8 -*-
from zipfile import ZipFile
from exception import excpt
from json import loads
import webbrowser
import urllib2
import help
import sys
import os


argum = set(['auth', 'upload', 'download'])


class SendData(object):

	ID = '10b419971c1142378516377c4b693bf9'
	ID_PASS = 'a0f40ea4db46466e87578c87e6aa77f4'
	TOKEN =''

	def __init__(self):
		if os.path.isfile('mytoken.dat'):
			token_file = open('mytoken.dat','rb')
			self.TOKEN = token_file.read(32)
			token_file.close()
		else:
			self.auth()

	@excpt
	def auth(self):
		request = urllib2.Request("".join(['https://oauth.yandex.ru/authorize?response_type=code&client_id=',self.ID,'&state=EnvTransfer']))
		url = urllib2.urlopen(request).geturl()
		webbrowser.open(url)
		code = raw_input('Enter your token:')
		self.TOKEN = self.post(code).read().split('"')[7]
		self.save_token(self.TOKEN)


	def save_token(self, token):
		with open('mytoken.dat','wb') as token_file:
			token_file.write(token)
		token_file.close()


	def get(self, url):
		request = urllib2.Request(url, headers={"Authorization" : " ".join(['OAuth',self.TOKEN])})
		return urllib2.urlopen(request).read()

	def post(self, code):
		data = "".join(['grant_type=authorization_code&code=',code,'&client_id=',self.ID,'&client_secret=',self.ID_PASS])
		data_len = len(data)
		request = urllib2.Request('http://oauth.yandex.ru/token', headers={	"Host": "oauth.yandex.ru",
																			"Content-type": "application/x-www-form-urlencoded",
																			"Content-Length": data_len})
		return urllib2.urlopen(request,data = data)
		

	@excpt
	def uploadFile(self,name):
		string	= self.get("".join(['https://cloud-api.yandex.net/v1/disk/resources/upload?path=',name,'&overwrite=true&fields=href']))
		read_file = open(name, 'rb')
		data = read_file.read()
		read_file.close()
		opener = urllib2.build_opener(urllib2.HTTPHandler)
		url = loads(string)['href'].encode('ascii')
		request = urllib2.Request(url, data=data)
		request.add_header('Content-Type', 'application/binary')
		request.get_method = lambda: 'PUT'
		url = opener.open(request)


	@excpt
	def downloadFile(self,name):
		string	= self.get("".join(['https://cloud-api.yandex.net/v1/disk/resources/download?path=',name,'&fields=href']))
		url = loads(string)['href']
		response = urllib2.urlopen(url)
		data = response.read()
		save_file = open(name, 'wb')
		save_file.write(data)
		save_file.close()

	@excpt
	def getArchive(self,name, path):
		with ZipFile(name, 'w') as archive:
			for root, dirs, files in os.walk(path):
				for file in files:
					if not file in name:
						archive.write(os.path.join(root, file))
		archive.close()

	@excpt
	def unRar(self,name):
		fh = open(name, 'rb')
		z = ZipFile(fh)
		for name in z.namelist():
		    outpath = os.getcwd()
		    z.extract(name, outpath)
		fh.close()
		z.close()

	def reEnter(self):
		token = raw_input('Refresh your token? (Y/n):')
		if token.lower() in 'y':
			self.auth()

def start():
	if len(sys.argv)>1 and sys.argv[1] in argum:
		data = SendData()
		command = sys.argv[1]
		if command in 'auth':
			data.reEnter()
		elif command in 'upload':
			abspath = os.getcwd().split('/')[-1].lower()
			file_name = "".join([abspath,'.zip'])
			data.getArchive(file_name, '../'+abspath)
			data.uploadFile(file_name)
		elif command in 'download':
			file_name = raw_input('Enter your envirenment name (example: myenv.zip): ').lower()
			data.downloadFile(file_name)
			data.unRar(file_name)
	else:
		help.show()