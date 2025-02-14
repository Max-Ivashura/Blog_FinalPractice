from sqlalchemy.orm import Session
from app.models import Comment
from app.models import User
from app.models import Post

def create_comment(db: Session, text: str, user_id: int, post_id: int):
    new_comment = Comment(text=text, user_id=user_id, post_id=post_id)
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment

def get_comments_by_post(db: Session, post_id: int):
    return db.query(Comment).filter(Comment.post_id == post_id).all()

def update_comment(db: Session, comment_id: int, text: str = None):
    comment = db.query(Comment).get(comment_id)
    if comment:
        if text:
            comment.text = text
        db.commit()
        db.refresh(comment)
    return comment

def delete_comment(db: Session, comment_id: int):
    comment = db.query(Comment).get(comment_id)
    if comment:
        db.delete(comment)
        db.commit()
    return comment