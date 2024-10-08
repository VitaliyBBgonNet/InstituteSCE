from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.config import DATABASE
from app.db.models.User import Base
from app.db.models.Type import Type
from app.db.models.Status import Status
from app.db.models.Project import Project
from app.db.models.Department import Department
from app.db.models.Details import Detail

DATABASE_URL = f"postgresql://{DATABASE['user']}:{DATABASE['password']}@{DATABASE['host']}:{DATABASE['port']}/{DATABASE['database']}"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    Base.metadata.create_all(bind=engine)
