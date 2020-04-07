from commandSystem.command import Command

class MenuCommand(Command):
    """
    Абстрактный класс команды главного меню
    """
    def __init__(self, player):
        super().__init__(player)


class PickCardCommand(MenuCommand):
    """
    Класс команды выбора карточки для дальнейших игр
    """
    def __init__(self, player, card_factory):
        super().__init__(player)
        self.card_factory = card_factory


class RemoveCardCommand(MenuCommand):
    """
    Класс команды убирания карточки из колоды для дальнейших игр
    """
    def __init__(self, player, card_factory):
        super().__init__(player)
        self.card_factory = card_factory


class NewUserCommand(MenuCommand):
    """
    Класс создания нового пользователя
    """
    def __init__(self, player=None):
        super().__init__(player)


class CreateGameCommand(MenuCommand):
    """
    Класс создания игры
    """
    def __init__(self, player, second_player):
        super().__init__(player)
        self.second_player = second_player