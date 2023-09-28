from sqlalchemy import select
from tables import users_table
from connect import engine

statement = select(users_table).where(users_table.c.name == 'Walter')



with engine.connect() as conn:
    result = conn.execute(statement)

    for row in result:
        print(row)  
        print(f"<Username: {row.name}, Fullname: {row.fullname}>")

