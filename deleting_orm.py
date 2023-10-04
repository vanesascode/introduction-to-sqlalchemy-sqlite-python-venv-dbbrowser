from session import session
from models import  User, Comment

# 2 ways to delete the same comment: 

# comment = session.query(Comment).filter_by(id = 1).first()
comment = session.query(Comment).filter(Comment.id == 1).first()

# First be sure of what you are going to delete!!
print(comment)

#Then delete: 
session.delete(comment)
session.commit()