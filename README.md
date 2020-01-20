# test_task


Install project:

    $ git clone https://github.com/shiryaev1/test_task.git
    $ cd test_task

Create database:

    $ sudo -u postgres psql postgres
    =# CREATE DATABASE test_db;
    =# CREATE USER developer WITH PASSWORD '123123qwe';
    =# ALTER ROLE developer SET client_encoding TO 'utf8';
    =# ALTER ROLE developer SET default_transaction_isolation TO 'read committed';
    =# ALTER ROLE developer SET timezone TO 'UTC';
    =# GRANT ALL PRIVILEGES ON DATABASE test_db TO developer;
    =# ALTER USER developer CREATEDB;
    
Install a virtual environment:

    $ virtualenv venv
    $ source venv/bin/activate 

Install requirements:

    (venv) $ pip install -r requirements.txt


Migrate the database before the first run:

    (venv) $ python manage.py migrate

Create a superuser:

    (venv) $ python manage.py createsuperuser


Load initial data for locations:

    (venv) $ python manage.py loaddata location/fixtures/location.json


### Running tests

    (venv) $ python manage.py test location.tests
    (venv) $ python manage.py test account.tests
    

### Running the application

    (venv) $ python manage.py runserver

The application should be visible at `127.0.0.1:8000` after that.

