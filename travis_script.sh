#!/bin/bash

# For each directory:
#  * remove venv
#  * create it 
#  * install using pip
#  * and run tox
for directory in 00_hello_world 01_todo_list 02_todo_list
do
  cd $directory
  rm -fr venv
  virtualenv -p python3 venv
  source venv/bin/activate
  tox
  deactivate
  cd .. 
done
