# ORM

from session import session
from models import User, Comment
from sqlalchemy import select, func

print()
print(">>>ALL USERS")
print()

users = session.query(User).all()
for user in users:
    print(user) 

###

print()
print(">>>ALL ORDER_BY ASC")
print()

users = session.query(User).order_by(User.username.asc()).all()
for user in users:
    print(user)

###

print()
print(">>>FILTER LIKE")
print()

users = session.query(User).filter(User.username.like('%Dantete%')).all()
for user in users:
    print(user)



###

print()
print(">>>THE FIRST, WITH FILTER_BY")
print()

users = session.query(User).filter_by(username = 'Nemito').all()
for user in users:
    print(user) # <User username=Nemito>

###

print()
print(">>>EXECUTE")
print()

result_proxy = session.execute(select(User).where(User.username == 'Dantete'))
for row in result_proxy:
    print(row)

###

print()
print(">>>SCALARS")
print()

scalar_result = session.scalars(select(func.count(User.id)).where(User.username == 'Dantete')).one()
print(scalar_result)

###

print()
print(">>>JOIN - all comments from a user - 1")
print()
statement = select(User, Comment).join(Comment).where(User.username == 'Dantete')

result = session.execute(statement).all()

for user, comment in result:
    print(f"Comment by {user.username}: {comment.text}")

# Comment by Dantete: This is a meow

###

print()
print(">>>JOIN - all comments from a user -2 ")
print()

user = session.query(User).filter_by(username='Pelusita').first()

if user:
    comments = session.query(Comment).filter_by(user=user).all()
    for comment in comments:
        print(comment) 
else:
    print("User not found")

# <Comment text=This is a comment by Pelusita>
# <Comment text=This is another comment by Pelusita>


