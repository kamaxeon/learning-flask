## Objetivo

En este caso el objetivo mínimo es tener una pequeña aplicación Rest. Para hacer lo más sencillo posible, no se usará las liberías de RestFull propias de flask.

La aplicación consistirá en una simple aplicación de tareas (ToDo List), no habrá persistencia, todo estará en memoria de la aplicación y una vez que paremos la aplicación todo se perderá.

Lo que también se introduce en esta parte es el uso de los códigos http, en la parte de enlaces puedes ver la referencia de Wikipedia.

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

* **title**: El título de la tarea (String)
* **description**: La description de la tarea (String)
* **done**: Indica el estado de la tarea (Boolean)

## Enlaces:

 * https://blog.miguelgrinberg.com/post/designing-a-restful-api-using-flask-restful
 * https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

## Pruebas

Lanzamos tox
