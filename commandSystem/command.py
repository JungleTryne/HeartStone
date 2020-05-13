class Command:
    """
    Абстрактный класс комманды.
    Реализуется паттерн команда
    """
    def __init__(self, player):
        self.player = player


class CommandFactory:
    """
    Фабрика комманд
    """
    def __init__(self):
        pass

    def get_command(self, user, *parameters):
        pass


class ParsingException(Exception):
    """Исключение ошибки распознавания команды"""
    pass
