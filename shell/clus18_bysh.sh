#!/bin/bash

# This is a script to update CLUS DevNet scripts on the Workstation Laptops.
# There is a bit.ly shortened URL that will redirect here bit.ly/byrneshoe
# The script can be copied to the workshop with 'curl -L -o filename.sh bit.ly/byrneshoe'

echo
echo Running Git Pull for ciscolive2018-byrne
cd ~/workspace/ciscolive2018-brybyrne
git pull
echo

echo Creating ~/workspace/rshoemak
cd ~/workspace
mkdir rshoemak && cd rshoemak
echo

echo Cloning DevNet2556
git clone https://www.github.com/rshoemak/DevNet2556/
echo

echo Cloning CL-Startup
git clone https://www.github.com/rshoemak/CL-Setup