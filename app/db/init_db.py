# app/db/init_db.py
from app.db.session import engine, Base
# Создание таблиц в базе данных
def create_tables():
    Base.metadata.create_all(bind=engine)

create_tables()