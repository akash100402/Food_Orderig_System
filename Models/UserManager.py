from Models.User import User


class UserManager:
    __Users = []

    @classmethod
    def AddUser(cls, user):
        if isinstance(user, User):
            cls.__Users.append(user)
            print("You have been successfully registered. Please login to continue")
        else:
            print("Invalid User")

    @classmethod
    def FindUser(cls, mailid, pwd):
        for user in cls.__Users:
            if user.MailId == mailid and user.Password == pwd:
                return user
            else:
                print("User not exist")
