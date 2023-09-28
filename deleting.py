from sqlalchemy import delete
from tables import users_table
from connect import engine

statement = delete(users_table).where(users_table.c.name == 'Chusta')

with engine.connect() as conn:
    result = conn.execute(statement)
    conn.commit()