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
pip install django-crispy-forms`

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
`python manage.py flush $appname$`
or if you have django-extensions
`python manage.py reset_db`
