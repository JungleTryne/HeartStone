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


class ParsingException(Exception):
    """Исключение ошибки распознавания команды"""
    pass
