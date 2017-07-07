## Objetivo

Partimos del ejemplo [anterior](./02_todo_list), tenemos nuestra API para la lista de tareas, y ahora queremos meterle autentificación mediante tokens usando [jwt](https://jwt.io/). En esta iteración no vamos a usar ninguna librería de flask y jwt, usaremos la libería [jwt nativa](https://github.com/jpadilla/pyjwt) en python.

Los métodos del todo list que usen el verbo PUT, deberán estar autentificados. No existirá tampoco persistencia con la autentificación, estará todo en memoria.

Para esto usaremos dos nuevas estructuras, una para los usuarios, y otra para los sesiones que se han hecho logout y ya son consideradas como inválidas.


## API

### ToDo List

| Método HTTP | URI                       | Acción                        |
|-------------|---------------------------|-------------------------------|
|     GET     | /todo/api/tasks           | Obtiene una lista de tareas   |
|     GET     | /todo/api/tasks/[task_id] | Obtiene una tarea             |
|    POST     | /todo/api/tasks           | Crea una nueva tarea          |
|     PUT     | /todo/api/tasks/[task_id] | Actualiza una tarea existente |
|   DELETE    | /todo/api/tasks/[task_id] | Borra una tarea               |
|   DELETE    | /todo/api/tasks           | Borra todas las tareas        |

### Estructura de una tarea

La estructura que nos expondrá la api tendrá los siguiente campos:

* **uri**: La URI de la tarea (String)
* **title**: El título de la tarea (String)
* **description**: La description de la tarea (String)
* **done**: Indica el estado de la tarea (Boolean)

### Autentificación

| Método HTTP | URI                     | Acción                        |
|-------------| ------------------------|-------------------------------|
|     POST    | /todo/api/auth/register | Registra un nuevo usuario     |
|     POST    | /todo/api/auth/login    | Autentifica a un usuario      |
|     GET     | /todo/api/auth/status   | Obtiene el estado del usuario |
|     POST    | /todo/api/auth/logout   | Des autentifica al usuario    |

### Estructura de un usuario

* **login**: El login del usuario (String)
* **password**: La contraseña del usuario (String)

### Estructura de los tokens inválidos

* **token**: El token inválido en sí (String)
## Enlaces:

 * https://realpython.com/blog/python/token-based-authentication-with-flask/
 * https://keathmilligan.net/jwt-authentication-with-flask-and-angular-2-a-simple-end-to-end-example/
 * https://github.com/zillacode/Flask-JWT/blob/master/RestExample/views.py
 * http://steelkiwi.com/blog/jwt-authorization-python-part-1-practise/
 * https://github.com/realpython/flask-jwt-auth/blob/master/project/tests/test_auth.py
 * http://software.danielwatrous.com/jwt-based-authentication-in-python-bottle/

## Pruebas

Lanzamos tox
