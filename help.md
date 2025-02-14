### Download mysql workbench:
[mysql-workbench](https://dev.mysql.com/downloads/file/?id=509428)
### Install mysql server and mysql shell:
[mysql server](https://dev.mysql.com/downloads/mysql/)
 
### Install django and mysqlclient for python:
`pip install python-dotenv
pip install django
pip install django-import-export
pip install mysqlclient
pip install django-extensions
pip install django-crispy-forms
pip install celery-progress
pip install django-celery_results
pip install django-celery
pip install xslxwriter
pip install mysql
pip install mysql-connector-python
pip install openpyxl`

### To start new project:
`django-admin startproject $projectname$`

### add this in settings.py to connect to mysql db:
`DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mdss',
        'USER': 'mdss_user',
        'PASSWORD': 'mdss_user_1234',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}`
CREATE DATABASE mdss
GRANT ALL PRIVILEGES ON *.* TO 'mdss_user'@'localhost' WITH GRANT OPTION;
`python manage.py makemigrations`
`python manage.py migrate`
`python manage.py runserver $server ip or localhost$`

### Create superuser:
`python manage.py createsuperuser`
### This will prompt for username, email and password.

### To create new app:
`python manage.py startapp $appname$`

### autogenerate models
`python manage.py inspectdb --database $dbname$`

### dump data
`python manage.py dumpdata $appname$ > filename$`
`python manage.py dumpdata $appname$ --indent=4 > filename.json$`

### load data into db
`python manage.py loaddata $appname$ --indent=4 > filename.json$`

### remove db from app
To remove all databases along with the data from your schema and then re-migrate the 
databases do the following:
`python manage.py flush $appname$`
or if you have django-extensions:
`python manage.py reset_db`
* Remove/delete the migrations folder
`python manage.py makemigrations $appname$`
`python manage.py migrate`

### install redis for windows (This is used as a message broker between celery and django)
Follow the guide here:
https://medium.com/@mayank_goyal/how-to-install-redis-and-as-a-windows-service-f0ab2559a3b
This will install redis as a system service on windows.
To add Redis as a Windows Service :
`redis-server --service-install`

https://www.youtube.com/watch?v=CkR_gjlDH-4
This shows how to integrate redis with django

To run celery (we offload intesive tasks to celery workers to do async processing):
`celery -A pymdss worker -P threads -E -l info` or
`celery -A pymdss worker -P threads -E -l debug` (to start in debug mode)

Docker:
To access containers:
`docker exec -it [container] bash`
Shows all containers:
`docker ps -a`
