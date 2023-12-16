# Hey Hom

## API

### To create a virtual environment.

- Choose a folder.
- In a terminal, in the chosen folder, execute: **python -m venv venv**
- To activate the env: **Source venv/bin/activate**
- To install the requirements: **pip install -r requirements.txt**

## To save and load data from/in the DB, in a JSON format.

- At the same level where the **manage.py** file is, to save data: **python manage.py dumpdata > file_name.json**
- At the same level where the **manage.py** file is, to load data: **python manage.py loaddata file_name.json**

## How to execute the project.

1.- Download the folder hey_hom.

2.- Open a terminal in the folder and navigate to where the **manage.py** file is.

3.- Execute the migrations to create the DB with these commands: **python manage.py makemigrations** then **python manage.py migrate**.

4.- Once the DB is created, execute the next command to load some data in it: **python manage.py loaddata respaldo.json**.

5.- To se some endpoints.

To create or load info:

- http://127.0.0.1:8000/api/create/

To see the whole list of information available: (It only shows 5 per page).

- http://127.0.0.1:8000/api/list/

To se the detail of one:

- http://127.0.0.1:8000/api/detail/3

To update and see the data to be updated beforhand:

- http://127.0.0.1:8000/api/update/4

To delete one:

- http://127.0.0.1:8000/api/delete/5

## For scalability and maintainability

I usually divide the applications inside of a folder, to keep all the files readable.

In the main folder, I create a settings folder to divide a base, local and production files, and inside the base file, the readability in the django, local and third party apps is also visible.
