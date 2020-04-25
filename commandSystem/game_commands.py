from commandSystem.command import Command
from commandSystem.command import CommandFactory

from dataBase.database import DataBaseProxy

from unitSystem.unit_deserialization import UnitDeserializer


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
        self.victim_card = victim_card


class PutCardCommand(GameCommand):
    """
    Класс команды выкладывания карты на стол
    """

    def __init__(self, player, game, attacking_card):
        super().__init__(player, game)
        self.attacking_card = attacking_card


class GameCommandFactory(CommandFactory):
    """
    Фабрика игровых команд
    """

    def __init__(self):
        super().__init__()


class NextCommandFactory(GameCommandFactory):
    """
    Фабрика команды пропуска хода
    """

    def __init__(self):
        super().__init__()

    def get_command(self, user, parameters=None):
        db = DataBaseProxy()
        game = db.get_users_game(user)
        command = NextCommand(user, game)
        return command


class AttackCommandFactory(GameCommandFactory):
    """
    Фабрика команды атаки картой
    """

    def __init__(self):
        super().__init__()

    def get_command(self, user, parameters=None):
        db = DataBaseProxy()
        game = db.get_users_game(user)
        command = AttackCommand(user, game, UnitDeserializer
                                .deserialize(parameters[0]),
                                UnitDeserializer.deserialize(parameters[1]))
        return command


class PutCardCommandFactory(GameCommandFactory):
    """
    Фабрика команды вынесения карты
    """

    def __init__(self):
        super().__init__()

    def get_command(self, user, parameters=None):
        db = DataBaseProxy()
        game = db.get_users_game(user)
        command = PutCardCommand(user, game, UnitDeserializer
                                 .deserialize(parameters[0]))
        return command
