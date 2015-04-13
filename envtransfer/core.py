# -*- coding: utf-8 -*-
from zipfile import ZipFile
from exception import function_exception
from json import loads
import webbrowser
import settings
import urllib2
import help
import sys
import os


arguments = {'auth', 'upload', 'download'}


def save_token(token):
    settings.TOKEN = token
    with open(settings.token_file, 'wb') as token_file:
        token_file.write(token)


def post(code):
    data = "".join(
        ['grant_type=authorization_code&code=', code, '&client_id=', settings.ID, '&client_secret=', settings.ID_PASS])
    data_len = len(data)
    request = urllib2.Request('http://oauth.yandex.ru/token', headers={"Host": "oauth.yandex.ru",
                                                                       "Content-type": "application/x-www-form-urlencoded",
                                                                       "Content-Length": data_len})
    return urllib2.urlopen(request, data=data)


def get(url):
    request = urllib2.Request(url, headers={"Authorization": " ".join(['OAuth', settings.TOKEN])})
    return urllib2.urlopen(request).read()


def find_file():
    if os.path.isfile(settings.token_file):
        with open(settings.token_file, 'rb') as token_file:
            settings.TOKEN = token_file.read(32)


@function_exception
def auth():
    request = urllib2.Request(
        "".join(
            ['https://oauth.yandex.ru/authorize?response_type=code&client_id=', settings.ID, '&state=EnvTransfer']))
    url = urllib2.urlopen(request).geturl()
    webbrowser.open(url)
    code = raw_input('Enter your code:')
    save_token(post(code).read().split('"')[7])


@function_exception
def upload_file(name):
    string = get("".join(
        ['https://cloud-api.yandex.net/v1/disk/resources/upload?path=', name, '&overwrite=true&fields=href']))
    with open(name, 'rb') as read_file:
        data = read_file.read()
    opener = urllib2.build_opener(urllib2.HTTPHandler)
    url = loads(string)['href'].encode('ascii')
    request = urllib2.Request(url, data=data)
    request.add_header('Content-Type', 'application/binary')
    request.get_method = lambda: 'PUT'
    opener.open(request)


@function_exception
def download_file(name):
    string = get(
        "".join(['https://cloud-api.yandex.net/v1/disk/resources/download?path=', name, '&fields=href']))
    url = loads(string)['href']
    response = urllib2.urlopen(url)
    data = response.read()
    with open(name, 'wb') as save_file:
        save_file.write(data)


@function_exception
def get_archive(name, path):
    with ZipFile(name, 'w') as archive:
        for root, dirs, files in os.walk(path):
            for file_name in files:
                if not file_name in name:
                    archive.write(os.path.join(root, file_name))


@function_exception
def extract_archive(name):
    with open(name, 'rb') as file_handle:
        zipfile = ZipFile(file_handle)
        for name in zipfile.namelist():
            out_path = os.getcwd()
            zipfile.extract(name, out_path)
        zipfile.close()


def start():
    if len(sys.argv) > 1 and sys.argv[1] in arguments:
        find_file()
        command = sys.argv[1]
        if command in 'auth':
            auth()
        elif command in 'upload':
            abspath = os.getcwd().split('/')[-1].lower()
            file_name = "".join([abspath, '.zip'])
            get_archive(file_name, '.')
            upload_file(file_name)
        elif command in 'download':
            file_name = raw_input('Enter your environment name (example: myenv.zip): ').lower()
            download_file(file_name)
            extract_archive(file_name)
    else:
        help.show()