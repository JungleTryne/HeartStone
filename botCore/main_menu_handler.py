from botCore.message_handler import CommandExecutor


class MainMenuHandler(CommandExecutor):
    """
    Класс обработки команд, вызванных в главном меню игры
    """

    @staticmethod
    def execute_command(command, user) -> list:
        pass


class PickCardExecutor(CommandExecutor):
    """
    Обработка команды выбора карты для дальнейших игр
    """

    @staticmethod
    def execute_command(command, user) -> list:
        pass


class RemoveCardExecutor(CommandExecutor):
    """
    Обработка команды убирания карты из колоды для дальнейших игр
    """

    @staticmethod
    def execute_command(command, user) -> list:
        pass


class NewUserExecutor(CommandExecutor):
    """
    Обработка команды создания нового пользователя
    """

    @staticmethod
    def execute_command(command, user) -> list:
        pass