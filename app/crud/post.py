from sqlalchemy.orm import Session
from app.models import Post
from app.models import User
from app.models import Category

def create_post(db: Session, title: str, content: str, user_id: int, category_id: int):
    new_post = Post(title=title, content=content, user_id=user_id, category_id=category_id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_posts_by_user(db: Session, user_id: int):
    return db.query(Post).filter(Post.user_id == user_id).all()

def get_posts_by_category(db: Session, category_id: int):
    return db.query(Post).filter(Post.category_id == category_id).all()

def update_post(db: Session, post_id: int, title: str = None, content: str = None):
    post = db.query(Post).get(post_id)
    if post:
        if title:
            post.title = title
        if content:
            post.content = content
        db.commit()
        db.refresh(post)
    return post

def delete_post(db: Session, post_id: int):
    post = db.query(Post).get(post_id)
    if post:
        db.delete(post)
        db.commit()
    return post