from sqlalchemy import create_engine, text, Column, VARCHAR, INTEGER
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship, declarative_base

engine = create_engine("mysql+mysqldb://root:root@localhost/hbtn_0e_101_usa", echo=True)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(nullable=True)

Base.metadata.create_all(bind=engine)
with engine.connect() as connection:
    data = connection.execute(text('select "test"'))
    print(data.all())
