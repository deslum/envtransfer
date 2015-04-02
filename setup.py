#!/usr/bin/env python
from distutils.core import setup
from setuptools import setup, find_packages
import envtransfer

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), 'README.txt')).read()


setup(name='envtransfer',
      version=envtransfer.__version__,
      description='Transfer your environment between computers.',
      author='Yuri Bukatkin',
      author_email='iturs@yandex.ru',
      url='http://envtransfer.deslum.com/',
      packages=find_packages(),
      entry_points={
        'console_scripts':
            ['envtransfer = envtransfer.core:start']
        }
     )

