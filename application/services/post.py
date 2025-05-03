from infrastructure.database.repositories.generic import GenericRepository

class PostService:
    def __init__(self):
        self.repo = GenericRepository('posts')

    def create_post(self, user_id, content):
        data = {
            'user_id': user_id,
            'content': content,
            'created_at': 'NOW()'
        }
        self.repo.insert(data)
