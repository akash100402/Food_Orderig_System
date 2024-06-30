from Models.User import User

class UserManager:
    __Users=[]
    @classmethod
    def AddUser(cls,user):
        if isinstance(user, User):
            cls.__Users.append(user)
        