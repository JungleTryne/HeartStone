from unitSystem.unit_base import Unit, UnitFabric


class UnitFractionOne(Unit):
    """
    Класс юнитов первой фракции
    :param: hp_rate - количество hp карточки
    :param: attack_rate - урон карточки
    :param: mana_rate - цена использования карточки
    :param: card_id уникальный ID карточки
    """
    def __init__(self, hp_rate: int, attack_rate: int,
                 mana_rate: int, card_id: int):
        super().__init__(hp_rate, attack_rate, mana_rate, card_id)


class UnitFractionOneFabric(UnitFabric):
    def __init__(self):
        super().__init__()
