# app/crud/category.py

from sqlalchemy.orm import Session
from app.models.category import Category

def create_category(db: Session, name: str):
    new_category = Category(name=name)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

def get_category_by_id(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()

def update_category(db: Session, category_id: int, name: str = None):
    category = db.query(Category).get(category_id)
    if category:
        if name:
            category.name = name
        db.commit()
        db.refresh(category)
    return category

def delete_category(db: Session, category_id: int):
    category = db.query(Category).get(category_id)
    if category:
        db.delete(category)
        db.commit()
    return category