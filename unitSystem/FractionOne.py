from unitSystem.unitBase import Unit, UnitFabric


class UnitFractionOne(Unit):
    """
    Класс юнитов первой фракции
    :param: hpRate - количество hp карточки
    :param: attackRate - урон карточки
    :param: manaRate - цена использования карточки
    :cardID: уникальный ID карточки
    """
    def __init__(self, hpRate: int, attackRate: int, manaRate: int, cardID: int):
        super().__init__(hpRate, attackRate, manaRate, cardID)


class UnitFractionOneFabric(UnitFabric):
    def __init__(self):
        super().__init__()
