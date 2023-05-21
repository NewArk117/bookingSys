from account import Account

class AccountController:
    def __init__(self):
        self.entity = Account()

    def get_username(self, user_id):
        return self.entity.get_username(user_id)

    def update_account_info(self, user_id, new_user_id, new_username):
        self.entity.update_account_info(user_id, new_user_id, new_username)

    def get_password(self, user_id):
        return self.entity.get_password(user_id)

    def update_password(self, user_id, new_password):
        self.entity.update_password(user_id, new_password)

    def close_connection(self):
        self.entity.close_connection()
