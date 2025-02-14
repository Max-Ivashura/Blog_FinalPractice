# main.py

from sqlalchemy.orm import sessionmaker
from app.database import engine
from app.crud import user, category, post, comment
from app.filters import filter_posts_by_date
from datetime import datetime

from app.models import Base

# Создаем таблицы (если их еще нет)
Base.metadata.create_all(bind=engine)
Base.registry.configure()

# Создаем сессию
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

# 1. Создание данных
print("Создание данных...")
alice = user.create_user(db, username="Alice", email="alice@example.com")
tech_category = category.create_category(db, name="Technology")
post1 = post.create_post(db, title="First Post", content="Hello world!", user_id=alice.id, category_id=tech_category.id)
comment1 = comment.create_comment(db, text="Great post!", user_id=alice.id, post_id=post1.id)

# 2. Чтение данных
print("\nЧтение данных...")
print(f"Пользователь: {alice}")
print(f"Категория: {tech_category}")
print(f"Пост: {post1}")
print(f"Комментарий: {comment1}")

# 3. Обновление данных
print("\nОбновление данных...")
updated_user = user.update_user(db, user_id=alice.id, email="new.alice@example.com")
updated_post = post.update_post(db, post_id=post1.id, title="Updated Post Title")
print(f"Обновленный пользователь: {updated_user}")
print(f"Обновленный пост: {updated_post}")

# 4. Фильтрация данных
print("\nФильтрация данных...")
start_date = datetime(2023, 1, 1)
end_date = datetime.now()
filtered_posts = filter_posts_by_date(db, start_date=start_date, end_date=end_date)
print(f"Посты за период: {filtered_posts}")

# 5. Удаление данных
print("\nУдаление данных...")
deleted_post = post.delete_post(db, post_id=post1.id)
deleted_user = user.delete_user(db, user_id=alice.id)
print(f"Удаленный пост: {deleted_post}")
print(f"Удаленный пользователь: {deleted_user}")