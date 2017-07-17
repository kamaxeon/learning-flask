## Objetivo

Partimos del ejemplo [anterior](./04_todo_list), ya tenemos funcionando el todo list con jwt, pero nuestro fichero [app.py](./04_todo_list/app.py) ya tiene casi 250 líneas y puede que empiece a ser un poco complejo de manejar.

En esta iteración, vamos a separar nuestro varios ficheros y vamos introducir el concepto de [blueprints en flask](http://flask.pocoo.org/docs/0.12/blueprints/), la idea es que tener nuestra aplicación lo más modular posible y poder reusar los componentes en el futuro.

Como pasó en la iteración anterior, debemos respetar los tests, y sólo cambiaremos la ubicación del código de la aplicación, pero no los tests en sí.


## API

### ToDo List

| Método HTTP | URI                       | Acción                        | Requiere token |
|-------------|---------------------------|-------------------------------|----------------|
|     GET     | /todo/api/tasks           | Obtiene una lista de tareas   | No             |
|     GET     | /todo/api/tasks/[task_id] | Obtiene una tarea             | No             |
|    POST     | /todo/api/tasks           | Crea una nueva tarea          | Sí             |
|     PUT     | /todo/api/tasks/[task_id] | Actualiza una tarea existente | Sí             |
|   DELETE    | /todo/api/tasks/[task_id] | Borra una tarea               | No             |
|   DELETE    | /todo/api/tasks           | Borra todas las tareas        | No             |

### Estructura de una tarea

La estructura que nos expondrá la api tendrá los siguiente campos:

* **uri**: La URI de la tarea (String)
* **title**: El título de la tarea (String)
* **description**: La description de la tarea (String)
* **done**: Indica el estado de la tarea (Boolean)

### Autentificación

| Método HTTP | URI                     | Acción                        | Requiere token |
|-------------| ------------------------|-------------------------------|----------------|
|     POST    | /todo/api/auth/register | Registra un nuevo usuario     | No             |
|     POST    | /todo/api/auth/login    | Autentifica a un usuario      | No             |
|     GET     | /todo/api/auth/status   | Obtiene el estado del usuario | Sí             |
|     POST    | /todo/api/auth/logout   | Des autentifica al usuario    | Sí             |
|    DELETE   | /todo/api/auth/register | Borra todos los usuarios      | No             |

### Estructura de un usuario

* **login**: El login del usuario (String)
* **password**: La contraseña del usuario (String)

### Estructura de los tokens inválidos

* **token**: El token inválido en sí (String)
## Enlaces:

 * http://exploreflask.com/en/latest/blueprints.html

## Pruebas

Lanzamos tox
