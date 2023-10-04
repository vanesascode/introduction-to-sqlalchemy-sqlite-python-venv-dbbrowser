# CORE

from connect import engine
from tables import meta_obj, users_table, comments_table

print(">>>CREATE DATABASE")
meta_obj.create_all(bind=engine)