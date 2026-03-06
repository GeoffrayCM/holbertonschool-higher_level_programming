#!/usr/bin/python3
"""State class definition for SQLAlchemy ORM"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

# Crée l'instance Base
Base = declarative_base()

class State(Base):
    """State class linked to table 'states'"""
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
