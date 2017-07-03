## Objetivo

Partimos del ejemplo [anterior](../01_todo_list), tenemos unos test que nos valen perfectamente. La idea es cambiar la parte de la aplicación usando las librerías de [Flask-RestFul](flask-restful.readthedocs.org/)

## API

| Método HTTP | URI                       | Acción                        |
|-------------|---------------------------|-------------------------------|
|     GET     | /todo/api/tasks           | Obtiene una lista de tareas   |
|     GET     | /todo/api/tasks/[task_id] | Obtiene una tarea             |
|    POST     | /todo/api/tasks           | Crea una nueva tarea          | 
|     PUT     | /todo/api/tasks/[task_id] | Actualiza una tarea existente | 
|   DELETE    | /todo/api/tasks/[task_id] | Borra una tarea               |
|   DELETE    | /todo/api/tasks           | Borra todas las tareas        |

## Estructura de una tarea

La estructura que nos expondrá la api tendrá los siguiente campos:

* **uri**: La URI de la tarea (String)
* **title**: El título de la tarea (String)
* **description**: La description de la tarea (String)
* **done**: Indica el estado de la tarea (Boolean)

## Enlaces:

 * https://blog.miguelgrinberg.com/post/designing-a-restful-api-using-flask-restful
 * https://tutorials.technology/tutorials/59-Start-a-flask-project-from-zero-building-api-rest.html
 * https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

## Pruebas

Lanzamos tox
