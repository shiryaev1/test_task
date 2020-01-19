# test_task


Install project:

    $ git clone https://github.com/shiryaev1/test_task.git
    $ cd test_task

Create database:

    $ sudo -u postgres psql postgres
    =# CREATE DATABASE test_db;
    
Install a virtual environment:

    $ virtualenv venv
    $ source venv/bin/activate 

Install requirements:

    pip install -r requirements.txt


Migrate the database before the first run:

    python manage.py migrate

Create a superuser:

    python manage.py createsuperuser


Load initial data for locations:

    python manage.py loaddata location/fixtures/location.json


### Running tests

    python manage.py test location.tests
    python manage.py test account.tests
    

### Running the application

    python manage.py runserver

The application should be visible at `127.0.0.1:8000` after that.

