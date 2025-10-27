Questo progetto ha scopo puramente didattico.

### TODO:
- add auth (JWT)
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

- genera secret key per auth
```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
# Output: kJ8Hn3L9pQ2mR5tW7xZ1aB4cD6eF8gH0
```

- Crea un superuser (impostazione guidata):

```bash
python manage.py createsuperuser
# Username: admin
# Email: admin@example.com
# Password: ****
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


```bash
curl -X GET http://127.0.0.1:8000/tasks/ \
-H "Content-Type: application/json" \
-H "Authorization: Bearer <access_token>"
```

```bash
curl -X POST http://127.0.0.1:8000/api/token/ \
-H "Content-Type: application/json" \
-d '{"username": "USER_NAME", "password": "PASSWORD"}'
```