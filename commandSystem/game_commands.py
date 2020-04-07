from commandSystem.command import Command


class GameCommand(Command):
    """
    Абстрактный класс команды на игровом поле
    """
    def __init__(self, player, game):
        super().__init__(player)
        self.game = game


class NextCommand(GameCommand):
    """
    Класс команды передачи хода другому игроку
    """
    def __init__(self, player, game):
        super().__init__(player, game)


class AttackCommand(GameCommand):
    """
    Класс команды атаки вражеской карточки
    """
    def __init__(self, player, game, attacking_card, victim_card):
        super().__init__(player, game)
        self.attacking_card = attacking_card
        self.victing_card = victim_card


class PutCardCommand(GameCommand):
    """
    Класс команды выкладывания карты на стол
    """
    def __init__(self, player, game, attacking_card):
        super().__init__(player, game)
        self.attacking_card = attacking_card
