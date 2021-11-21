# wheatley-api
API for wheatley app


## Stack
- Python 3
- Django REST Framework



# How to, all python django stuff
To go inside virtual env
```
source venv/bin/activate
```

To install deps
```
pip install -r requirements.txt
```

To save deps
```
pip freeze > requirements.txt
```


## Some cmds


creating apps
```
python manage.py startapp nameoftheapp
```

update db with migration
```
python manage.py migrate
```

creating migrations from models
```
python manage.py makemigrations
```

create superuser
```
python manage.py createsuperuser
```


## access to objects from terminal
```
python3 manage.py shell
```
