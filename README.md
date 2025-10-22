### TODO:
- add DRF (DJago Rest Framework)
	- add DTO / Mapper (serializer)
	- add annotation (get and post request) to the view

- create a new entity
```bash
python manage.py startapp <entity name>

```

- create a new migration
```bash
python manage.py makemigrations 

```

- apply migrations 
```bash
python manage.py migrate

```

## SQLite

- Inspect db throught Django
```bash
python manage.py dbshell

```

- Inspect db
```bash
sqllite3 db.sqlite3 # db is the db name

```

- Format code
```bash
ruff format .

```

- Check imports
```bash
ruff check .

```


