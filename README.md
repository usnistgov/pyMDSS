# pyMDSS

A Python/Django version of the Measurements and Database System (MDSS). It is a web app for uploading, searching and exporting calibration measurement data (standard resistors, quantized conductance and capacitors). Data is stored in MySQL. Large uploads are processed in the background by Celery workers that use Redis as the message broker.

```
pyMDSS/
├── pymdss/              Django project root (manage.py lives here)
│   ├── pymdss/          settings, urls, celery config
│   ├── resistors/       standard-resistor app (upload, search, export)
│   ├── qconductance/    quantized-conductance app
│   ├── capacitors/      capacitor app (work in progress)
│   ├── templates/  static/  media/
├── start_pymdss.bat          launch web server (HTTP)
├── start_pymdss_secure.bat   launch web server (HTTPS)
└── start_celery.bat          launch Celery worker
```

## Prerequisites

| Component | Notes |
|---|---|
| Python 3.10–3.13 | Django 5.2 LTS supports these. Tested with 3.12 |
| MySQL Server 8.0 or later | [Download](https://dev.mysql.com/downloads/mysql/). [MySQL Workbench](https://dev.mysql.com/downloads/workbench/) is optional but useful |
| Redis | Message broker between Django and Celery. It must listen on `localhost:6379`. On Windows, install it as a service ([guide](https://medium.com/@mayank_goyal/how-to-install-redis-and-as-a-windows-service-f0ab2559a3b)). That Windows port is Redis 3.0, which only works with redis-py below 6, so the install command below pins it |
| mkcert (optional) | Only for HTTPS. See [mkcert releases](https://github.com/FiloSottile/mkcert/releases) |

## 1. Install Python dependencies

From the repository root, create a virtual environment and install the packages:

```bash
python -m venv .venv
```

```bash
.venv\Scripts\activate
```

```bash
pip install "django>=5.2,<5.3" python-dotenv mysqlclient mysql-connector-python whitenoise django-extensions celery "redis>=5.0.3,<6" django-celery-results celery-progress openpyxl xlsxwriter werkzeug pyopenssl
```

## 2. Create the MySQL database and user

In the MySQL shell or Workbench, run:

```sql
CREATE DATABASE mdss CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'mdss_user'@'localhost' IDENTIFIED BY '<choose-a-password>';
GRANT ALL PRIVILEGES ON mdss.* TO 'mdss_user'@'localhost';
FLUSH PRIVILEGES;
```

## 3. Create the `.env` file

`settings.py` reads the Django secret key and the database connection details from environment variables through `python-dotenv`. Create `pymdss/pymdss/.env` (next to `settings.py`) with the lines below. `pymdss/.env` next to `manage.py` also works, but if both exist the one next to `settings.py` wins.

```ini
DJANGO_SECRET_KEY=<long-random-string>
DB_NAME=mdss
DB_USER=mdss_user
DB_USER_PASSWORD=<choose-a-password>
DB_HOST=localhost
```

Generate the secret key with:

```bash
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

If people reach the server by a host name that isn't listed in `ALLOWED_HOSTS` in `settings.py`, add it (comma-separated for several) instead of editing the code:

```ini
DJANGO_EXTRA_ALLOWED_HOSTS=myhost.campus.nist.gov
```

> `.env` must never be committed. Without it, every `manage.py` command fails with
> `ImproperlyConfigured: DJANGO_SECRET_KEY is not set`.
>
> After changing `.env`, fully restart the web server and the Celery worker. The web server's
> automatic reload keeps the old values.

## 4. Initialize the database

### Option A: restore from a backup

If you have a `mysqldump` backup (for example `pymdss_db_bak_YYYY-MM-DD.sql`), check what it contains before you load it:

```bash
findstr /B /C:"-- Current Database:" pymdss_db_bak_YYYY-MM-DD.sql
```

If it lists only `mdss`, import the whole file. If it also lists `mysql` (an `--all-databases` dump), **do not import the whole file**: that would overwrite this server's user accounts and system tables. Instead, copy the dump's first 20 lines (the header) plus everything from the `-- Current Database: `mdss`` line up to the next `-- Current Database:` line (or the end of the file) into a new file, and import only that:

```bash
mysql -u mdss_user -p mdss < mdss_only.sql
```

Then run `python manage.py migrate` (from `pymdss/`) to apply any migrations the backup is missing. The backup already contains the user accounts, so you can log in with your existing username.

### Option B: start with an empty database

```bash
cd pymdss
```

```bash
python manage.py migrate
```

```bash
python manage.py createsuperuser
```

`createsuperuser` asks for a username, email and password. You use this account to log in to the app and to the admin at `/admin/`.

## 5. Run the app

Start Redis first, then start these two processes, each in its own terminal (both from the `pymdss/` folder with the venv activated).

**Celery worker.** Handles file uploads. Uploads stay pending until it is running.

```bash
celery -A pymdss worker -P threads -E -l info
```

Use `-l debug` for more detailed logs.

**Web server.** The settings ship with `DEBUG = False` and `SECURE_SSL_REDIRECT = True`. That means plain HTTP requests are redirected to HTTPS, so you have to pick one of these two modes:

### Option A: HTTPS (matches `start_pymdss_secure.bat`)

Generate a certificate once with mkcert. Add every hostname or IP that users will type:

```bash
mkcert-v1.4.4-windows-amd64.exe -cert-file cert.pem -key-file key.pem localhost 127.0.0.1 pymdss.campus.nist.gov
```

Then run:

```bash
python manage.py runserver_plus --cert-file cert.pem --key-file key.pem 0.0.0.0:8000
```

Open https://localhost:8000.

> **Warning:** `runserver_plus` always turns on the Werkzeug debugger. Anyone who can reach the server can open its
> interactive console at `/console`, protected only by the PIN printed in the terminal. Use it only on a trusted network,
> and don't run the server on `0.0.0.0` where untrusted machines can reach it.

### Option B: HTTP for local development

Set `DEBUG = True` in `pymdss/pymdss/settings.py`. This turns off the HTTPS redirect. Then run:

```bash
python manage.py runserver 127.0.0.1:8000
```

Open http://127.0.0.1:8000.

### Static files when `DEBUG = False`

WhiteNoise serves static files. After you change anything in `static/`, rebuild them:

```bash
python manage.py collectstatic
```

### Windows shortcuts

The `start_*.bat` files in the repository root run the commands above. They `cd` into a hard-coded path (`C:\Users\ohm\Desktop\pyMDSS\pymdss`), so change that path to match your checkout before you use them.

## Using the app

1. Log in on the home page with the superuser, or with any user created in `/admin/`. Every other page requires logging in.
2. Choose a calibration area (Resistors or Quantized Conductance).
3. **Upload** pipe-delimited (`|`) MDSS data files. Processing runs in Celery and a progress bar shows its status. A file whose name was already uploaded is skipped.
4. **Search** by serial, nominal value, process or service ID, then download the results as `.xlsx`.
5. **Documentation** shows the row count for each table.

## Useful maintenance commands

Run these from `pymdss/`:

| Task | Command |
|---|---|
| Create migrations after model changes | `python manage.py makemigrations` |
| Export an app's data | `python manage.py dumpdata resistors --indent=4 > resistors.json` |
| Load exported data | `python manage.py loaddata resistors.json` |
| Delete all rows (keeps tables) | `python manage.py flush` |
| Drop and recreate the whole DB | `python manage.py reset_db` (django-extensions) |
| Generate models from an existing DB | `python manage.py inspectdb` |

See [help.md](help.md) for the original setup notes.

## Troubleshooting

| Symptom | Cause |
|---|---|
| `DJANGO_SECRET_KEY is not set` | `pymdss/pymdss/.env` is missing, or has no `DJANGO_SECRET_KEY` line |
| `'NoneType' object has no attribute 'startswith'` | The DB variables in `.env` are missing or misspelled |
| `Access denied for user 'mdss_user'@'localhost'` right after changing `.env` | The web server or Celery worker is still using the old password. Stop and start them again |
| `Bad Request (400)` | The host name in the address bar isn't allowed. Add it to `DJANGO_EXTRA_ALLOWED_HOSTS` in `.env` |
| `Error 10061 connecting to localhost:6379` | Redis is not running |
| `MySQL 8.4 or later is required (found 8.0.x)` | Django 6 is installed. Run `pip install "django>=5.2,<5.3"` |
| `unknown command 'HELLO'` | redis-py 6 or later is installed but the Redis server is 3.x. Run `pip install "redis>=5.0.3,<6"` |
| Uploads stay at 0% | The Celery worker is not running |
| Browser is redirected to `https://` and the connection fails | You ran `runserver` with `DEBUG = False`. Use Option A or Option B above |
| CSS is missing when `DEBUG = False` | Run `python manage.py collectstatic` |
