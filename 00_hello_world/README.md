## Objetivo

* Tener un proyecto mínimo para que arranque Flask
* Tener un test
* Usar buenas prácticas de estilo, mediante [pylint](https://www.pylint.org/) y [flake8](http://flake8.pycqa.org/en/latest/)

## Uso
Simplemente la aplicación de flask con un simple 'Hello Wolrd!'

```
cd 00_hello_world
python app.py
```

## Pruebas

- Lanzamos tox  
Debería pasar todos los test

- Desde otra terminal, lanzamos curl:  
Debería devolver una cadena, para la respuesta html, y un json para la respuesta
json
    - `curl http://localhost:5000/hello_world`         (html response)
    - `curl http://localhost:5000/api/hello_world`     (json response)

