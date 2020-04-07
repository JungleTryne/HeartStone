class Command:
    """
    Абстрактный класс комманды.
    Реализуется паттерн команда
    """
    def __init__(self, player):
        self.player = player
