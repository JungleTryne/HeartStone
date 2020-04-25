from botCore.command_executor import CommandExecutor
from commandSystem.main_menu_command import PickCardCommand, RemoveCardCommand, CreateGameCommand, ChangeFractionCommand
from botCore.message_answer import MessageAnswer
from dataBase.database import DataBaseProxy
from botCore.game import Game


class WrongPlace(Exception):
    pass


class MainMenuHandler(CommandExecutor):
    """
    Класс обработки команд, вызванных в главном меню игры
    """

    @staticmethod
    def execute_command(command) -> list:
        if command.player.current_game is not None:
            return [MessageAnswer(command.player, 'Нельзя изменять игрока во время игры')]

        if isinstance(command, PickCardCommand):
            return PickCardExecutor.execute_command(command)
        if isinstance(command, RemoveCardCommand):
            return RemoveCardExecutor.execute_command(command)
        if isinstance(command, CreateGameCommand):
            return NewGameExecutor.execute_command(command)
        if isinstance(command, ChangeFractionCommand):
            return ChangeFractionExecutor.execute_command(command)
        raise WrongPlace


class ChangeFractionExecutor(CommandExecutor):
    """
    Класс обработки команды смены фракции
    """
    @staticmethod
    def execute_command(command) -> list:
        if not command.fraction:
            return [MessageAnswer(command.player, 'Ошибка в ChangeFractionExecutor')]
        command.player.fraction = command.fraction
        command.player.card_set_selected = list()
        db = DataBaseProxy()
        db.update_user(command.player.vk_id, command.player)
        return [MessageAnswer(command.player, 'Фракция успешно изменена')]


class PickCardExecutor(CommandExecutor):
    """
    Обработка команды выбора карты для дальнейших игр
    """

    @staticmethod
    def execute_command(command) -> list:
        if not command.card_factory:
            return [MessageAnswer(command.player, 'Ошибка в PickCardExecutor')]
        if command.card_factory in command.player.card_set_selected:
            return [MessageAnswer(command.player, 'Карта уже в колоде')]

        command.player.card_set_selected.append(command.card_factory)
        db = DataBaseProxy()
        db.update_user(command.player.vk_id, command.player)
        return [MessageAnswer(command.player, 'Карта успешно добавлена в колоду')]


class RemoveCardExecutor(CommandExecutor):
    """
    Обработка команды убирания карты из колоды для дальнейших игр
    """

    @staticmethod
    def execute_command(command) -> list:
        try:
            command.player.card_set_selected.remove(command.card_factory)
        except:
            pass

        db = DataBaseProxy()
        db.update_user(command.player.vk_id, command.player)
        return [MessageAnswer(command.player, 'Карта успешно удалена из колоды')]


class NewGameExecutor(CommandExecutor):
    """
    Обработка команды создания новой игры
    """

    @staticmethod
    def execute_command(command: CreateGameCommand) -> list:
        if command.second_player is None:
            return [MessageAnswer(command.player, 'Второй игрок не найден')]

        command.player.hp_rate = 100
        command.second_player.hp_rate = 100

        game = Game(command.player, command.second_player)

        command.player.current_game = game
        command.second_player.current_game = game

        db = DataBaseProxy()
        db.update_user(command.player.vk_id, command.player)
        db.update_user(command.second_player.vk_id, command.second_player)

        return [MessageAnswer(command.player, 'Игра началась'),
                MessageAnswer(command.second_player, 'Игра началась')]
