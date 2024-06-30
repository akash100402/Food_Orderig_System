from Models.User import User
from Models.UserManager import UserManager


class LoginSystem:

    def Login(self):
        mailid = input("Your email: ")

        password = input("Your password: ")

        user = UserManager.FindUser(mailid, password)

        if user is not None:
            print("User logged in successfully")
        else:
            print("Invalid email or password. Try again...")

    def Register(self):
        print("Register to Food app")
        name = input("Your name: ")

        mobile = int(input("Your mobile number: "))

        mailid = input("Your email: ")
        password = input("Your password: ")

        user = User(name, mobile, mailid, password)
        UserManager.AddUser(user)

    def GuestLogin(self):
        pass

    def ValidateOption(self, option):
        if option == 1:
            self.Login()
        elif option == 2:
            self.Register()
        elif option == 3:
            self.GuestLogin()
        else:
            print("Thank you, visit again😊")
            exit()


class FoodApp:
    LoginOptions = {1: "Login", 2: "Register", 3: "Guest", 4: "Exit \n"}

    @staticmethod
    def Init():
        print("--Welcome to Online Food Ordering--")

        while True:
            loginSystem = LoginSystem()

            for option in FoodApp.LoginOptions:
                print(f"{option}.{FoodApp.LoginOptions[option]}", end=" ")
            choice = int(input("Enter your choice: "))
            try:
                print(f"Your choice is => {FoodApp.LoginOptions[choice]}")
                loginSystem.ValidateOption(choice)
            except ValueError:
                print("Invalid Choice......Please enter valid choice")
