# app/models/post.py

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.models.base import Base
from datetime import datetime

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))

    # Отношения
    author = relationship('User', back_populates='posts')  # Связь с User
    category = relationship('Category', back_populates='posts')  # Связь с Category
    comments = relationship('Comment', back_populates='post', cascade="all, delete-orphan")  # Связь с Comment

    def __repr__(self):
        return f"<Post(id={self.id}, title='{self.title}', author='{self.author.username if self.author else None}')>"