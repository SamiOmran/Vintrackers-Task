# Vinitrackers System
This built using django-rest framework [django-rest Framework](https://www.django-rest-framework.org/)

## Steps

### Initialize a virtual environment

**Windows**:
```
$ python3 -m venv venv
$ venv\Scripts\activate
```

**Unix/MacOS**:
```
$ python3 -m venv venv
$ source venv/bin/activate
```

 
### Add Environment Variables

Create `.env` file that contains environment variables. **Very important: do not include the `.env` file in any commits. This should remain private.** You will manually maintain this file locally, and keep it in sync on your host.
You need to set these variables:
- SECRET_KEY
- DEBUG
- and database configurations


### Installation
install all required packages and django-rest framework run:
```
$ pip install -r requirements.txt
```


### Run the application
1- edit the .env file for you database credentials

using `python manage.py migrate` run migration files

2- run the server:
```
$ python manage.py runserver
```

server is up and running:
```
* Performing system checks...

* System check identified no issues (0 silenced).
* December 18, 2024 - 22:29:07
* Django version 5.1.4, using settings 'vehicle_service.settings'
* Starting development server at http://127.0.0.1:8000/
* Quit the server with CTRL-BREAK.
```

