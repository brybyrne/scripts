#! /bin/bash

yum install -y gcc zlib-devel openssl-devel
cd /usr/src
wget https://www.python.org/ftp/python/2.7.14/Python-2.7.14.tgz
tar xzf Python-2.7.14.tgz
cd Python-2.7.14
./configure
make altinstall

cd /usr/src
wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tgz
tar xzf Python-3.6.2.tgz
cd Python-3.6.2
./configure
make altinstall
