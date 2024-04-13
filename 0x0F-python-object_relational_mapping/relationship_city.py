#!/usr/bin/python3
""" a python file that contains the class definition of
a State and an instance Base = declarative_base() """

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """
    Class with id and name attributes of each city
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True,
                autoincrement=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
