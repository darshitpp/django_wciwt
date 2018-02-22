### Where can I watch this?
wciwt makes it easier to find your favourite TV shows and movies in India. It hopes to support Netflix, Prime Video and Hotstar in the near future.

### Requirements
* Python 3
* Postgres 10.2
* Heroku(for pulling the database)
* Every module listed in the "requirements.txt"

### Installation
* Clone repository from Heroku ```heroku git:clone -a app_name```
* Switch to virtualenv: ```source virtualenv_location/bin/activate```
* Install necessary modules: ```pip install -r requirements.txt```
* Login to Heroku
* Pull the database from Heroku: ```heroku pg:pull database_name local_database_name --app appname```
* Start serving Django: ```python manage.py runserver```

### Participation
Contact [@dronethrone](https://t.me/dronethrone/) for more information.

wciwt is available on the Python Package Index (PyPI) at [https://pypi.python.org/pypi/wciwt](https://pypi.python.org/pypi/wciwt)

### Heroku
Hosted on Heroku here: [https://testwciwt.herokuapp.com/](https://testwciwt.herokuapp.com/)