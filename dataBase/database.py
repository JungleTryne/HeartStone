from botCore.user import User
from unitSystem.fraction_one import UnitFractionOne

class DataBaseProxy:
    class __DataBaseProxy:
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

        def update_user(self, vk_id, user_object):
            self.vk_dict[vk_id] = user_object

        def get_users_game(self, user):
            if user in self.game_dict:
                return self.game_dict[user]
            return None

        def register_user(self, vk_id):
            new_user = User(vk_id, UnitFractionOne, list(), list(), None, None)
            self.vk_dict[vk_id] = new_user
            return new_user

    instance = None

    def __new__(cls):
        if not DataBaseProxy.instance:
            DataBaseProxy.instance = DataBaseProxy.__DataBaseProxy()
        return DataBaseProxy.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)
