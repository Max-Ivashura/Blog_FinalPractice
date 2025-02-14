from sqlalchemy.orm import Session
from app.models.post import Post

from datetime import datetime


def filter_posts_by_date(db: Session, start_date: datetime, end_date: datetime):
    return db.query(Post).filter(
        Post.created_at >= start_date,
        Post.created_at <= end_date
    ).all()
