from botCore.command_executor import CommandExecutor
from botCore.message_answer import MessageAnswer


class UnknownCommandHandler(CommandExecutor):
    """
    Класс обработки неизвестной команды
    """

    @staticmethod
    def execute_command(command) -> list:
        return UnknownCommandExecutor.execute_command(command)


class UnknownCommandExecutor(CommandExecutor):
    """
    Класс отправки сообщения об ошибке о неизвестной команде
    """

    @staticmethod
    def execute_command(command) -> list:
        return [MessageAnswer(command.user, 'Неизвестная команда!')]
