from UserModel import Base
from db import engine

def init_db():
    Base.metadata.create_all(bind=engine)

init_db()