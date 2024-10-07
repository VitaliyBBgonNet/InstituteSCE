# db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE

DATABASE_URL = f"postgresql://{DATABASE['user']}:{DATABASE['password']}@{DATABASE['host']}:{DATABASE['port']}/{DATABASE['database']}"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
