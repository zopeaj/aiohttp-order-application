from sqlalchemy.orm import Session

class UserRepository:
    def __init__(self):
        self.db = Session()

    def save(user: User):
        user = User()
        user.setUsername(user.getUserName())
        self.db.commit(user)
        self.db.flush()

    def getByUsername(username: str):
        user = self.db.get(User).filter(User.getusername(), username)
        if user:
            return user
        return None

    def findUserById(userId: int):
        user = self.db.query(User).filter(User.getId() == userId)
        if user is not None:
            return user
        return None

    def delete(username: str):
        user = self.db.get(User).filter(username, username)
        if user:
            self.db.delete(user)
            self.db.commit()
        return None




