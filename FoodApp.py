class LoginSystem:
    pass


class FoodApp:
    LoginOptions={1:"Login", 2: "Register", 3:"Guest", 4: "Exit \n"}
    @staticmethod
    def Init():
        print("--Welcome to Online Food Ordering--")
        for option in FoodApp.LoginOptions:
            print(f"{option}.{FoodApp.LoginOptions[option]}", end=" ")
        choice=int(input("Enter your choice: "))
        if 1<=choice<=4:
            print(f"Your choice is => {FoodApp.LoginOptions[choice]}")
        else:
            print("Invalid Choice")