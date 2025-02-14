# app/models/comment.py

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.models.base import Base
from datetime import datetime

class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))

    # Отношения
    author = relationship('User', back_populates='comments')  # Связь с User
    post = relationship('Post', back_populates='comments')  # Связь с Post

    def __repr__(self):
        return f"<Comment(id={self.id}, text='{self.text[:20]}...', author='{self.author.username if self.author else None}')>"