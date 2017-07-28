#!/bin/bash

# PROYECTS=(00_hello_world 01_todo_list 02_todo_list 03_todo_list 04_todo_list)
PROYECTS=(00_hello_world)

# For each proyect:
#  * remove venv
#  * create it
#  * install using pip
#  * and run tox

for DIRECTORY in ${PROYECTS[*]}
do
    cd ${DIRECTORY}
    echo -e "cd ${DIRECTORY} → `pwd`\n\n"

    rm -fr venv
    echo -e "Delete 'venv' in ${DIRECTORY} directory.\n\n"

    virtualenv -p python3 venv
    echo -e "Re-Create 'venv' environment in ${DIRECTORY}.\n\n"

    source venv/bin/activate
    echo -e "Activate 'venv' environment in ${DIRECTORY} proyect.\n\n"

    if [ ${DIRECTORY} == "00_hello_world" ]; then
        pip install pip-tools -U
        pip-compile --output-file requirements-prod.txt requirements-prod.in
        pip install -r requirements-prod.txt -U
        pip-compile --output-file requirements-dev.txt requirements-dev.in
        pip install -r requirements-dev.txt -U
        echo -e "Installed requeriment for ${DIRECTORY}\n\n"
    else
        pip install -r requirements.txt
        echo -e "Installed requeriment for ${DIRECTORY}\n\n"
    fi
    echo -e "Installed full requeriment for ${DIRECTORY}.\n\n"

    tox
    echo -e "Tox ejecuted.\n\n"

    deactivate
    echo -e "Deactivate of 'venv' environment of ${DIRECTORY}.\n\n"

    cd ..
done
