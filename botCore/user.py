class User:
    """
    Объект пользователя игры
    По факту является датаклассом
    """
    def __init__(self, fraction, card_set_selected, card_set_current, current_game=None, hp_rate=None):
        self.fraction = fraction
        self.card_set_selected = card_set_selected
        self.card_set_current = card_set_current
        self.current_game = current_game
        self.hp_rate = hp_rate
