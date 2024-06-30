from Models.User import User
from Models.UserManager import UserManager

class LoginSystem:

    def Login(self):
        pass

    def Register(self):
        print("Register to Food app")
        name=input("Your name: ")
        email=input("Your email: ")
        mobile=int(input("Your mobile number: "))
        password=input("Your password: ")
        
        user=User(name,email,mobile,password)
        UserManager.AddUser(user)
        

    def GuestLogin(self):
        pass

    def ValidateOption(self, option):
        if option==1:
            self.Login()
        elif option == 2:
            self.Register()
        elif option==3:
            self.GuestLogin()
        else:
            print("Thank you, visit again😊")
            exit()


class FoodApp:
    LoginOptions = {1: "Login", 2: "Register", 3: "Guest", 4: "Exit \n"}

    @staticmethod
    def Init():
        print("--Welcome to Online Food Ordering--")

        loginSystem=LoginSystem()

        for option in FoodApp.LoginOptions:
            print(f"{option}.{FoodApp.LoginOptions[option]}", end=" ")
        choice = int(input("Enter your choice: "))
        if 1 <= choice <= 4:
            print(f"Your choice is => {FoodApp.LoginOptions[choice]}")
            loginSystem.ValidateOption(choice)
        else:
            print("Invalid Choice")
