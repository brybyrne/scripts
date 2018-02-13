#!/bin/bash

echo What is the path to your new repository?

read DESTVAR
echo
echo
echo Copying .gitignore and requirements.txt
cp -vr /Users/brybyrne/code/scripts/shell/prep_env/files/ $DESTVAR/
echo
echo
cd $DESTVAR
mv -v gitignore .gitignore


