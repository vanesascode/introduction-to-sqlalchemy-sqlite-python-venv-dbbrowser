from session import session
from models import User, Comment

# 2 different ways to update the same comment: 

# comment = session.query(Comment).filter(Comment.id == 1).first()

comment = session.query(Comment).filter_by(id = 1).first()

comment.text = "This is an updated comment again"

session.commit()