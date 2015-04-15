
###EnvTransfer - transfer your environment between computers using Yandex disk.

[![Build Status](https://travis-ci.org/deslum/envtransfer.svg)](https://travis-ci.org/deslum/envtransfer)
[![Downloads](https://pypip.in/d/envtransfer/badge.svg)](https://pypi.python.org/pypi/envtransfer)

Requirements
============

* Python 2.7
* Works on Linux, Windows, Mac OSX, BSD

##Installation

``` 
1. Create a Python virtual environment and activate it

    $ virtualenv venv
    $ source venv/bin/activate

2. Install package

    $ pip install https://github.com/deslum/envtransfer/archive/master.zip

or

    $ pip install envtransfer

``` 

##Using

  Get token

``` 
$ envtransfer auth
``` 

  Upload environment

``` 
$ envtransfer upload
``` 

  Download environment

``` 
$ envtransfer download
``` 
