from account import Account

class AccountController:
    def __init__(self):
        self.entity = Account()

    def get_username(self, user_id):
        return self.entity.get_info(user_id)

    def is_user_id_exists(self, user_id):
        return self.entity.is_user_id_exists(user_id)


    def update_account_info(self, user_id, new_user_id, new_username, DOB):
        self.entity.update_account_info(user_id, new_user_id, new_username, DOB)
        self.entity.update_food_orders_user_id(user_id, new_user_id)
        self.entity.update_ticket_user_id(user_id, new_user_id)

    def get_password(self, user_id):
        return self.entity.get_password(user_id)

    def update_password(self, user_id, new_password):
        self.entity.update_password(user_id, new_password)
