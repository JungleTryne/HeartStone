from botCore.user import User


class DataBaseProxy:
    def __init__(self):
        raise NotImplementedError

    def get_user_by_vk_id(self, vk_id):
        raise NotImplementedError

    def get_users_game(self, user):
        raise NotImplementedError
