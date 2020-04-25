from commandSystem.command import Command
from commandSystem.command import CommandFactory
from unitSystem.fraction_one import UnitFractionOne
from unitSystem.fraction_two import UnitFractionTwo
from unitSystem.unit_fabrics import UnitOneFabric, UnitTwoFabric, \
    UnitThreeFabric, UnitFourFabric

from dataBase.database import DataBaseProxy


class MenuCommand(Command):
    """
    Абстрактный класс команды главного меню
    """

    def __init__(self, player):
        super().__init__(player)


class MenuCommandFactory(CommandFactory):
    def __init__(self):
        super().__init__()


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


class CreateGameCommand(MenuCommand):
    """
    Класс создания игры
    """

    def __init__(self, player, second_player):
        super().__init__(player)
        self.second_player = second_player


class ChangeFractionCommand(MenuCommand):
    """
    Команда смены фракции
    """

    def __init__(self, player, fraction):
        super().__init__(player)
        self.fraction = fraction


class ChangeFractionCommandFactory(MenuCommandFactory):
    def __init__(self):
        super().__init__()

    def get_command(self, user, parameters=None):
        if not parameters:
            return ChangeFractionCommand(user, None)
        if parameters[0] == 'one':
            return ChangeFractionCommand(user, UnitFractionOne)
        if parameters[0] == 'two':
            return ChangeFractionCommand(user, UnitFractionTwo)
        return ChangeFractionCommand(user, None)


class PickCardCommandFactory(MenuCommandFactory):
    def __init__(self):
        super().__init__()

    def get_command(self, user, parameters=None):
        if not parameters:
            return PickCardCommand(user, None)
        if user.fraction == UnitFractionOne and parameters[0] == "one":
            return PickCardCommand(user, UnitOneFabric)
        if user.fraction == UnitFractionOne and parameters[0] == "two":
            return PickCardCommand(user, UnitTwoFabric)
        if user.fraction == UnitFractionTwo and parameters[0] == "three":
            return PickCardCommand(user, UnitThreeFabric)
        if user.fraction == UnitFractionTwo and parameters[0] == "four":
            return PickCardCommand(user, UnitFourFabric)
        return PickCardCommand(user, None)


class CreateGameCommandFactory(MenuCommandFactory):
    def __init__(self):
        super().__init__()

    def get_command(self, user, parameters=None):
        if not parameters:
            return CreateGameCommand(user, None)
        db = DataBaseProxy()
        other_user = db.get_user_by_vk_id(parameters[0])
        return CreateGameCommand(user, other_user)


class RemoveCardCommandFactory(MenuCommandFactory):
    def __init__(self):
        super().__init__()

    def get_command(self, user, parameters=None):
        if not parameters:
            return RemoveCardCommand(user, None)
        if user.fraction == UnitFractionOne and parameters[0] == "one":
            return RemoveCardCommand(user, UnitOneFabric)
        if user.fraction == UnitFractionOne and parameters[0] == "two":
            return RemoveCardCommand(user, UnitTwoFabric)
        if user.fraction == UnitFractionTwo and parameters[0] == "three":
            return RemoveCardCommand(user, UnitThreeFabric)
        if user.fraction == UnitFractionTwo and parameters[0] == "four":
            return RemoveCardCommand(user, UnitFourFabric)
        return RemoveCardCommand(user, None)
