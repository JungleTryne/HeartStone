from commandSystem.command import Command


class UnknownCommand(Command):
    """
    Класс неизвестной комманды
    """
    def __init__(self, user):
        self.user = user
