class Game:
    """
    Объект игры
    """
    def __init__(self, user_one, user_two):
        """
        :param user_one: Первый игрок
        :param user_two: Второй игрок
        """
        self.user_one = user_one
        self.user_two = user_two
        self.turn = user_one
        self.field = list()
