from models.user_model import UserModel


class UserController:
    def __init__(self) -> None:
        self.user_model = UserModel()

    def check_if_name_is_registered(self, name):
        return self.user_model.name_exists(name)

    def check_if_email_is_registered(self, email):
        return self.user_model.email_exists(email)