from commandSystem.game_commands import AttackCommandFactory, PutCardCommandFactory, NextCommandFactory
from commandSystem.main_menu_command import PickCardCommandFactory, CreateGameCommandFactory, NewUserCommandFactory, RemoveCardCommandFactory
from commandSystem.unknown_command import UnknownCommand

from commandSystem.command import ParsingException


class CommandCreatorHandler:
    """
    Класс обработки сырого сообщения, возвращается объект Command
    """
    router = {
        # Game commands
        '/put': PutCardCommandFactory,
        '/attack': AttackCommandFactory,
        '/next': NextCommandFactory,

        # Main menu commands
        '/pick_card': PickCardCommandFactory,
        '/create_game': CreateGameCommandFactory,
        '/register': NewUserCommandFactory,
        '/remove_card': RemoveCardCommandFactory,
    }

    @staticmethod
    def get_command(message, user):
        nonlocal router
        try:
            command = router[message[0]].get_command(user, message[1:])
            return command
        except ParsingException:
            return UnknownCommand()
