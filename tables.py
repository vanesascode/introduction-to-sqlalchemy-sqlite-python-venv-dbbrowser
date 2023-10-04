# CORE

from sqlalchemy import Table, MetaData, Column
from sqlalchemy import Integer, String, Text, ForeignKey


meta_obj = MetaData()

users_table = Table(
  "users",
  meta_obj,
  Column("id", Integer, primary_key=True),
  Column("name", String(50), nullable=False),
  Column("fullname", Text),

)

comments_table = Table(
  "comments",
  meta_obj,
  Column("id", Integer, primary_key=True),
  Column("comment", Text, nullable=False),
  Column("user_id", Integer, ForeignKey("users.id")),
)