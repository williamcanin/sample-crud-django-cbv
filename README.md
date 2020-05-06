## Sample CRUD Django Framework using Class-Based Views

![Python package](https://github.com/williamcanin/simple-crud-django-cbv/workflows/Python%20package/badge.svg)

This repository contains a sample [Django](https://www.djangoproject.com/) crud using Class-Based Views. The project has no style sheet development, just pure html.

## Develop and Tests

```shell
$ python -m venv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
$ pytest
```

## Run in browser

```shell
$ ./manage.py makemigrations
$ ./manage.py migrate
$ ./manage.py createsuperuser
$ ./manage.py runserver
```
