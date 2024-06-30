from Models.FoodItem import FoodItem
from Models.Restaurant import Restaurant
from Models.FoodMenu import FoodMenu

class FoodManager:
    def __init__(self):
        self.Restaurants=[]

    def PrepareFoodItems(self):
        item1=FoodItem("Chicken Briyani",4,190,"sdfghjk")
        item2 = FoodItem("Curd Rice", 3.9, 60, "oasdfa")
        item3 = FoodItem("Veg Meals", 4.8, 160, "dfadhff0masdc")
        item4 = FoodItem("bucket Briyani", 5, 470, "nonod8oasdgw")
        item5 = FoodItem("Beef curry", 4.5, 210, "sdfdasgdf8adffajonib")

    def PrepareFoodMenus(self):
        menu1=FoodMenu("Veg")
        menu2=FoodMenu("Non-Veg")
        menu3=FoodMenu("Western")

    def PrepareRestaurants(self):

        res1=Restaurant("A2B",5,"Chennai",10)
        res1=Restaurant("Firdous",4.8,"Mumbai",15)
        res1=Restaurant("Hirabdhi Briyani",4.3,"Hydrabad",22)