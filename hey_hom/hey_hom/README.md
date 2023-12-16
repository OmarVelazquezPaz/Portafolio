# Hey Hom

## API

### Crear una ambiente virtual.

- Seleccionar una carpeta.
- En una terminal dentro de la carpeta seleccionada, ejecutar: **python -m venv venv**
- Para activar el ambiente viertual: **Source venv/bin/activate**
- Instalar los reuerimientos del proyecto: **pip install -r requirements.txt**

## Para guardar y cargar información de/en la base de datos en un formato JSON.

- Al nivel donde se encantra en archivo **manage.py** para guardar datos, ejecutar: **python manage.py dumpdata > nom_archivo.json**
- Al nivel donde se encantra en archivo **manage.py** para cargar datos, ejecutar : **python manage.py loaddata nom_archivo.json**

## Instrucciones para ejecutar el proyecto.

1.- Descargar el proyecto.

2.- Entrar a la carpeta hey_home.

3.- Ejecutar las migraciones para crear la base de datos, **python manage.py makemigrations** despues **python manage.py migrate**.

4.- Una vez creada la base de datos ejecutar el siguiente comando para llenar la base con algunos ejemplos **python manage.py loaddata respaldo.json**.

5.- Ejemplos para ver los endpoints.

Para crear:

- http://127.0.0.1:8000/api/create/

Para ver toda la lista de datos: (Solo se muestran 5 en cada pagina).

- http://127.0.0.1:8000/api/list/

Detalle de uno en especifico:

- http://127.0.0.1:8000/api/detail/3

Para actualizar los datos de una entrada:

- http://127.0.0.1:8000/api/update/4

Para borrar datos:

- http://127.0.0.1:8000/api/delete/5
