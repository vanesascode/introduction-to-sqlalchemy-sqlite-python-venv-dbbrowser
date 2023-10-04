# ORM

from models import User, Comment
from session import session

Pelusa = User(
  username='Pelusita',
  email_address = 'pelusa@me.com',
  comments = [
    Comment(
      text = 'This is a comment',
    ),
    Comment(
      text = 'This is another comment',
    )
  ]
)

Dante = User(
  username='Dantete',
  email_address = 'Dante@me.com',
  comments = [
    Comment(
      text = 'This is a meow',
    )
  ]
)

Nemo = User(
  username='Nemito',
  email_address = 'nemo@me.com',
)

session.add_all([Pelusa, Dante, Nemo])
session.commit()

