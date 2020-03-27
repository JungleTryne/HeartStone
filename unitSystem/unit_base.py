from heartstoneUtils.id_generator import IDGenerator


class Unit:
    """
    Unit Base class
    :param: hp_rate - количество hp карточки
    :param: attack_rate - урон карточки
    :param: mana_rate - цена использования карточки
    :param: card_id уникальный ID карточки
    """

    def __init__(self, hp_rate: int, attack_rate: int, mana_rate: int, card_id: int):
        self.hp_rate = hp_rate
        self.attack_rate = attack_rate
        self.mana_rate = mana_rate
        self.card_id = card_id

    def __del__(self):
        IDGenerator().remove_id(self.card_id)

    def is_alive(self) -> bool:
        """
        Функция, возвращает true, если юнит ещё жив
        :return: Жив ли юнит
        """
        return self.hp_rate > 0

    def attack(self, another_unit) -> bool:
        """
        Функция атаки на юнит. Возвращает true, если юнит еще жив
        :param another_unit: Атакующий юнит
        :return: Жив ли юнит
        """
        self.hp_rate -= another_unit.attack_rate
        return self.hp_rate > 0


class UnitFabric:
    def __init__(self):
        pass

    def get_card(self) -> Unit:
        """
        Функция получение карточки типа Unit
        """
        pass
