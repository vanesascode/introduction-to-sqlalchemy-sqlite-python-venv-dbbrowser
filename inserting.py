# CORE

from sqlalchemy import insert
from tables import users_table
from connect import engine

statement = insert(users_table)

# print(statement)

with engine.connect() as conn:
    conn.execute(statement, [
        {'name': 'Walter', 'fullname': 'White'},
        {'name': 'Lizz', 'fullname': 'Ginger'},
    ])
    conn.commit()

