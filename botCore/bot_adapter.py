import vk_api
from datetime import datetime
import random

from secret.keys import _vk_token


class BotAdapter:
    """
    Класс адаптера под бота. Бот для вк еще не выбран
    """
    @staticmethod
    def send_message(user, message, api):
        print('[{0}] Отправляем пользователю {1} сообщение \"{2}\"'
              .format(str(datetime.now())[:-7], user.vk_id, message))

        api.messages.send(user_id=int(user.vk_id),
                             message=message,
                             random_id=random.randint(0, 2**64-1))
