from botCore.command_executor import CommandExecutor


class UnknownCommandHandler(CommandExecutor):
    """
    Класс обработки неизвестной команды
    """

    @staticmethod
    def execute_command(command) -> list:
        pass


class UnknownCommandExecutor(CommandExecutor):
    """
    Класс отправки сообщения об ошибке о неизвестной команде
    """

    @staticmethod
    def execute_command(command) -> list:
        pass
