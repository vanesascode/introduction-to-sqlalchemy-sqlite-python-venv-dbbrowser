# CORE + ORM

### TO SEE VERSION: 

# import sqlalchemy
# print(sqlalchemy.__version__)

### TO CREATE ENGINE:

from sqlalchemy import create_engine, text

### CONNECTION TO THE DATABASE: 

engine = create_engine('sqlite:///sample2.db', echo=True)

### TEST: 

# with engine.connect() as conn:
#     result = conn.execute(text('SELECT "Hello"'))
 
#     print(result.all())