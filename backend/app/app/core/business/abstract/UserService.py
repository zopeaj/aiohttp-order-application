from app.models.user import User
from app.db.base import Base
from app.crud.user_repository import UserRepository

class UserService:
    def __init__(self, userRespository):
        self.userRespository: UserRepository = userRespository

    def create(self, user: User):
        pass

    def update(self, user: User):
        pass

    def getByUsername(self, user: User):
        pass

    def delete(self, user_id: User):
        pass


