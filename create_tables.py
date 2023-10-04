# ORM

from models import Base
from connect import engine

print(">>>CREATE TABLES>>>>")
Base.metadata.create_all(bind=engine)