from botCore.user import User


class DataBaseProxy:
    """
    Класс прокси для базы данных
    На данны момент реализован лишь в оперативке
    """

    def __init__(self):
        self.vk_dict = dict()
        self.game_dict = dict()

    def get_user_by_vk_id(self, vk_id):
        if vk_id in self.vk_dict:
            return self.vk_dict[vk_id]
        return None

    def get_users_game(self, user):
        if user in self.game_dict:
            return self.game_dict[user]
        return None

    def register_user(self, vk_id):
        new_user = User(0, tuple(), tuple(), None, None)
        self.vk_dict[vk_id] = new_user
        return new_user
