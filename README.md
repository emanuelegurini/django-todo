### TODO:
 - Models Not Registered in Admin
 - improve error handling

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

- run server
```bash
python manage.py runserver  

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


