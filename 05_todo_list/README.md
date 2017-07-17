## Objetivo

Partimos del ejemplo [anterior](./03_todo_list), hemos introducido el concepto de tokens usando [jwt](https://jwt.io/), la implementación la hemos realizado con la librería [pyjwt](https://github.com/jpadilla/pyjwt). En esta iteración, se intentará reemplazar nuestra implementación inicial por la librería [flask-jwt-extended](https://github.com/vimalloc/flask-jwt-extended).

Los métodos del todo list que usen el verbo PUT, deberán estar autentificados. No existirá tampoco persistencia con la autentificación, estará todo en memoria.

Los tests se intentarán mantener lo máximo posible, y sólo se deberán cambiar cuando la librería que usemos tenga un comportamiento diferente al anterior.


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

 * https://github.com/vimalloc/flask-jwt-extended/tree/master/examples

## Pruebas

Lanzamos tox
