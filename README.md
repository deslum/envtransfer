
###EnvTransfer - transfer your environment between computers using Yandex disk.

[![Build Status](https://travis-ci.org/deslum/envtransfer.svg)](https://travis-ci.org/deslum/envtransfer)


##Installation

``` 
1. Create a Python virtual environment and activate it

    If Pip and virtual environments are not installed
    
        a) $ wget https://bootstrap.pypa.io/get-pip.py
        b) $ python get-pip.py
        c) $ pip install virtualenv
        
    $ virtualenv venv
    $ source venv/bin/activate

2. Install package

    $ pip install https://github.com/deslum/envtransfer/archive/master.zip
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
