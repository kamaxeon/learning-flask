#!/bin/bash

PROYECTS=(00_hello_world 01_todo_list 02_todo_list 03_todo_list 04_todo_list)

# For each proyect:
#  * remove venv
#  * create it
#  * install using pip
#  * and run tox

for DIRECTORY in ${PROYECTS[*]}
do
    cd ${DIRECTORY}
    rm -fr venv
    virtualenv -p python3 venv
    if [ ${DIRECTORY} == "00_hello_world" ]; then
        pip install pip-tools -U
        pip-compile --output-file requirements-prod.txt requirements-prod.in
        pip install -r requirements-prod.txt -U
        pip-compile --output-file requirements-dev.txt requirements-dev.in
        pip install -r requirements-dev.txt -U
    else
        pip install -r requirements.txt
    fi
    source venv/bin/activate
    tox
    deactivate
    cd ..
done
