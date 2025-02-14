from sqlalchemy import create_engine
from app.models.base import Base

engine = create_engine("sqlite:///blog.db", echo=True)

# Проверяем, что таблицы существуют
print(Base.metadata.tables.keys())
