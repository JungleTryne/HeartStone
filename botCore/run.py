import vk_api
from botCore.bot_adapter import BotAdapter
from vk_api.longpoll import VkLongPoll, VkEventType
from botCore.message_handler import MessageHandler

from secret.keys import _vk_token


def longpoll_listening() -> None:
    """ Стартер прослушки запросов боту
    """
    vk = vk_api.VkApi(token=_vk_token)
    api = vk.get_api()
    longpoll = VkLongPoll(vk)
    print('Начали слушать сервачок')
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                messages = MessageHandler.handle_request(str(event.message), str(event.user_id))
                for message in messages:
                    BotAdapter.send_message(message.user, message.message, api)


if __name__ == '__main__':
    longpoll_listening()