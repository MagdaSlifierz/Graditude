import uuid

from sqlalchemy import Column, Integer, String, DateTime
from gratitude_journal.models.database import Base
from datetime import datetime

"""
    This module Represents a User entity within the database.
"""


class User(Base):
    """
    User entity model representing a user in the database.
    """

    __tablename__ = "users"

    id = Column(Integer, nullable=False, primary_key=True)
    unique_id = Column(String, nullable=False, default=lambda: str(uuid.uuid4()))
    username = Column(String, unique=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String)
    full_name = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.now)
