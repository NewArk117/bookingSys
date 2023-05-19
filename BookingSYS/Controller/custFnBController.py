from fnb import FnB

class FoodController:
    def get_food(self):
        food_data = FnB.get_food(self)
        return food_data
