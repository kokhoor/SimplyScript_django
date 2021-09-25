# SimplyScript Django

The purpose of this project is to manage the permissions for the django-auth service in SimplyScript, which is a scripting framework for applications.

## Installing SimplyScript Django

### 1. Clone SimplyScript Django

* Clone  SimplyScript to your favourite folder, e.g. /opt/projects/

     ```git clone https://github.com/kokhoor/SimplyScript_django.git```

### 2. Create Python Virtual Environment

* To install, first ensure that you have python 3.8 or higher installed

* Create a new python virtualenv using:

     ```python -m venv [virtualenv folder]```

    for example:

     ```python -m venv /opt/venv/simplyscript```

* If not activated, change to the virtualenv using:

     ```source /opt/venv/simplescript/bin/activate```

* Ensure you're in the SimplyScript_django folder, and install the required python libraries into your virtual environment using following command:

     ```pip install -r docs/requirements.txt```

### 3. Setup the settings file

* Create your settings file in: ```simplyscript_django/settings_local.py```. This can be used to put in your database settings and will overwrite any settings in ```simplyscript_django/settings.py```.

* You can copy ```simplyscript_django/settings_local.py.sample``` to  ```simplyscript_django/settings_local.py```, and put in the SECRET_KEY as well as the default database settings.

### 4. Setup the database

* Ensure that the databse of your choice has been created (if required)

* Execute migrate while the simplyscript virtual environment is active and you're in the project folder using:

     ```python manage.py migrate```

* Create your superuser to enable login to admin

     ```python manage.py createsuperuser```

* To run a development webserver, use:

     ```python manage.py runserver```

     You can then browse to the admin page and do the necessary setup
