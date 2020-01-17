# test_task


Migrate the database before the first run:

    python manage.py migrate

Create a superuser:

    python manage.py createsuperuser

Install requirements:

    pip install -r requirements.txt

Load initial data for projects:

    python manage.py loaddata location/fixtures/location.json


### Running tests

    python manage.py test location.tests
    python manage.py test account.tests
    

### Running the application

    python manage.py runserver

The application should be visible at `127.0.0.1:8000` after that.

