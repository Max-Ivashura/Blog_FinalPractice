from sqlalchemy import Column, Integer, String
from app.models.base import Base

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f"<Category(id={self.id}, name='{self.name}')>"