class MessageHandler:
    """
    Класс обработки сообщения пользователя.
    Является статическим
    """

    @staticmethod
    def handle_request(message, vk_id) -> list:
        """
        Обработка сырого запроса. Использует СommandCreatorHandler, чтобы получить
        объект команды пользователя для последующей передачи handle_command
        """
        pass

    @staticmethod
    def handle_command(command) -> list:
        """
        Непосредственная обработка команды
        """
        pass


class CommandExecutor:
    """
    Абстрактный класс обработки команд
    """

    @staticmethod
    def execute_command(command) -> list:
        pass
