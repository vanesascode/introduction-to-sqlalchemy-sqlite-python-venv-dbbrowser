from sqlalchemy import update
from tables import users_table
from connect import engine

# statement = update(users_table).where(users_table.c.name == 'Walter').values(name='Chusta')

statement = update(users_table).where(users_table.c.id == 5).values(name='Chusta', fullname='Ayerbe')

with engine.connect() as conn:
    result = conn.execute(statement)
    conn.commit()

# print(statement)