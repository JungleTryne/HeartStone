from botCore.command_executor import CommandExecutor


class GameHandler(CommandExecutor):
    """
    Класс обработки команд, вызванных во время игры
    """

    @staticmethod
    def execute_command(command) -> list:
        pass


class AttackCommandExecutor(CommandExecutor):
    """
    Класс обработки команды атаки на карточку противника
    """

    @staticmethod
    def execute_command(command) -> list:
        pass


class PlaceCommandExecutor(CommandExecutor):
    """
    Класс обработки команды выставления карты на игровой стол
    """

    @staticmethod
    def execute_command(command) -> list:
        pass


class NextCommandExecutor(CommandExecutor):
    """
    Класс обработки команды передачи хода
    """

    @staticmethod
    def execute_command(command) -> list:
        pass
