from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.models.base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)

    # Отношения
    posts = relationship('Post', back_populates='author', cascade="all, delete-orphan")  # Связь с Post
    comments = relationship('Comment', back_populates='author', cascade="all, delete-orphan")  # Связь с Comment

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"
