from sqlalchemy.orm import Session

class UserRepository:
    def __init__(self):

    def save(db: Session, user: User):
        user = User()
        user.setUsername(user.getUserName())
        db.add(user)
        db.commit(user)
        return user

    def getByUsername(db: Session, username: str):
        user = db.get(User).filter(User.getusername(), username)
        if user:
            return user
        return None

    def findUserById(db: Session, userId: int):
        user = db.query(User).filter(User.getId() == userId)
        if user is not None:
            return user
        return None

    def delete(db: Session, username: str):
        user = db.get(User).filter(username, username)
        if user:
            db.delete(user)
            db.commit()
        return None




