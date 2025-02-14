from chapter_6_final_projects.project_1_blog.app.models.user import User


def create_user(username, email):
    user = User(username, email)

