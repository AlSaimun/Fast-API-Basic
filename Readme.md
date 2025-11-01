

## Database Operations
alembic init -t async alembic
alembic revision --autogenerate -m "create table"
alembic upgrade head

## Run
fastapi dev app/main.py