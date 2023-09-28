from connect import engine
from tables import meta_obj, users_table, comments_table

### Create the tables

print(">>>CREATE DATABASE")
meta_obj.create_all(bind=engine)