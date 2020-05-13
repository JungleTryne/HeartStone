class MessageAnswer:
    """
    Класс ответа серверу пользователю
    """
    def __init__(self, user, message):
        self.user = user
        self.message = message
