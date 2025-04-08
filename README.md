# Task Manager
Проект создан с целью изучения фреймворка django. Реализована система аутентификации, создание и отображение задач зарегистрированным пользователям по дням недели.
## Dependencies

requirements.txt

## Install App with python

``` bash
git clone https://github.com/Rebarial/Task_Manager_Django
```
change SECRET_KEY in Task_Manager_Django/.env

``` bash
cd Task_Manager_Django

python -m pip install -r requirements.txt

python taskManager/manage.py makemigrations

python taskManager/manage.py migrate

python taskManager/manage.py runserver
```
## Install App with Docker
``` bash
git clone https://github.com/Rebarial/Task_Manager_Django
```
change SECRET_KEY in Task_Manager_Django/.env

Run Docker application if didnt do that
``` bash
cd Task_Manager_Django

docker build -t application_name .

docker run -it -p 8000:8000 application_name
```
## For google auth

Login admin panel with superuser (ip/admin)

(if havent superuser yet: <code>python taskManager/manage.py createsuperuser</code> and follow instruction)

Add soclial application. Fill fields: Provider, client id, secret key by google OAuth 2.0 Client

https://developers.google.com/identity/protocols/oauth2

##Preview

