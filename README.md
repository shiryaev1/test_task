Migrate the database before the first run:

    python manage.py migrate

Create a superuser:

    python manage.py createsuperuser

Load initial data for projects:

    python manage.py loaddata location/fixtures/location.json

### Running the application

    python manage.py runserver

The application should be visible at `127.0.0.1:8000` after that.

### Running tests

    python manage.py test location.tests


