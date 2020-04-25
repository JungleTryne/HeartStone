from dataBase.database import DataBaseProxy

from commandSystem.game_commands import GameCommand
from commandSystem.main_menu_command import MenuCommand

from botCore.command_creator_handler import CommandCreatorHandler
from botCore.main_menu_handler import MainMenuHandler
from botCore.game_handler import GameHandler
from botCore.unknown_command_handler import UnknownCommandHandler


class MessageHandler:
    """
    Класс обработки сообщения пользователя.
    Является статическим
    """

    @staticmethod
    def handle_request(message: str, vk_id: str) -> list:
        """
        Обработка сырого запроса. Использует СommandCreatorHandler, чтобы получить
        объект команды пользователя для последующей передачи в handle_command
        """
        message = message.split()
        db = DataBaseProxy()
        handler = CommandCreatorHandler()
        user = db.get_user_by_vk_id(vk_id)
        if user is None:
            user = db.register_user(vk_id)
        command = handler.get_command(message, user)
        answers = MessageHandler.handle_command(command)
        return answers


    @staticmethod
    def handle_command(command) -> list:
        if isinstance(command, MenuCommand):
            return MainMenuHandler.execute_command(command)
        elif isinstance(command, GameCommand):
            return GameHandler.execute_command(command)
        return UnknownCommandHandler.execute_command(command)


class CommandExecutor:
    """
    Абстрактный родительский класс обработки команд
    """

    @staticmethod
    def execute_command(command) -> list:
        pass
